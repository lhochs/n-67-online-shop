from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login_and_register")
def login_and_register():
    return render_template("login.html")

@app.route("/register", methods=["POST"])
def register():
    if not User.validate_register(request.form):
        return redirect("/login_and_register")
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "password":pw_hash,
        "role_type":request.form["role_type"]
    }
    user_id = User.save(data)
    session["user_id"] = user_id
    return redirect("/login_and_register")

@app.route("/login", methods=["POST"])
def login():
    if not User.validate_login(request.form):
        return redirect("/login_and_register")
    user = User.get_by_email(request.form)
    if user:
        if not bcrypt.check_password_hash(user.password, request.form["password"]):
            flash("The password you've entered is incorrect.")
            return redirect("/login_and_register")
        session["user_id"] = user.user_id
        return redirect("/")
    flash("The email you entered isn't connected to an account. Find your account and log in.")
    return render_template("/login_and_register")

@app.route("/signup")
def signup():
    return render_template("signup.html")

# This route can be used for both seller and buyer, based on user role
@app.route("/user/dashboard")
def dashboard():
    return render_template("dashboard.html")