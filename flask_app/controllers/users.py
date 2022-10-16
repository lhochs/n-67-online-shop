from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_app.models.user import User
from flask_app.models.order import Order
from flask_app.models.product import Product
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

########################################
#### This is where we set the route ####
########################################
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login_and_register")
def login_and_register():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

# user dashboard - show all the orders they have
@app.route("/user_dashboard")
def user_dashboard():
    # Check if user logs in and user has the same id as given customer_id
    if (not session):
        redirect("/login")

    user_data = {
        customer_id: session["user_id"]
    }
    orders = Order.get_all_orders_by_customer_id(user_data)

    return render_template("user_dashboard.html", orders=orders)

# seller dashboard - show all the products they have
@app.route("/seller_dashboard")
def seller_dashboard():
    if (not session):
        redirect("/")

    user_data = {
        seller_id: session["user_id"]
    }
    products = Product.get_all_products_by_seller_id(user_data)

    return render_template("seller_dashboard.html", products=products)


#####################################
#### This is where the API stays ####
#####################################

@app.route("/register", methods=["POST"])
def register():
    if not User.validate_register(request.form):
        return redirect("/login_and_register")
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "password":pw_hash
    }
    user_id = User.save(data)
    session["user_id"] = user_id
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    if not User.validate_login(request.form):
        return redirect("/login_and_register")
    user = User.get_by_email(request.form)
    if user:
        if not bcrypt.check_password_hash(user.password, request.form["password"]):
            flash("The password you've entered is incorrect.")
            return redirect("/login_and_register")
        session["user_id"] = user.id
        return redirect("/")
    flash("The email you entered isn't connected to an account. Find your account and log in.")
    return render_template()
