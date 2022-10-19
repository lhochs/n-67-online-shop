#from crypt import methods
from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.product import Product, User

########################################
#### This is where we set the route ####
########################################
# This is where user can add product
# @app.route("/")
# def index():
#     return render_template("index.html", all_products = Product.get_all())

@app.template_filter()
def currencyFormat(value):
    value = float(value)
    return "${:,.2f}".format(value)

@app.route("/user/new_product")
def new_product():
    if (not session):
        return redirect("/login_and_register")

    # If user is a buyer, redirect
    if (session["role_type"] == "customer"):
        return redirect("/")

    return render_template("add_form.html")

@app.route("/user/add_product_to_db", methods=['POST'])
def add_product_to_db():
    if (not session):
        return redirect("/login_and_register")
    if not Product.validate_product(request.form):
        return redirect('/user/new_product')
    data = {
        'product_name' : request.form["product_name"],
        'product_description' : request.form["product_description"],
        'product_instructions' : request.form["product_instructions"],
        'product_quantity' : request.form["product_quantity"],
        'price_per_unit' : request.form["price_per_unit"],
        'product_img' : request.form["product_img"],
        'seller_id' : session["user_id"]  
    }
    Product.save(data)
    print("jk here is the real issue")
    return redirect('/seller_dashboard')

# This is where user can edit product
# <<<<<<< HEAD
# @app.route("/user/edit_product/<id>")
# def edit_product(id):
#     return render_template("add_edit_product_form.html") //duplicate code what is this for?

#route to view one product
@app.route("/product/<id>")
def view_product(id):
    # if 'user_id' not in session:
    #     return redirect('/')
    # data = {
    #     "id": id
    # }
    # user_data = {
    #     "id": session['user_id']
    # }
    return render_template("view_one.html") #, product=Product.get_by_id(data), user=User.get_by_id(user_data))
    
# =======
@app.route("/user/edit_product/<product_id>")
def edit_product(product_id):
    # If user is not logged in, redirect
    if (not session):
        redirect("/login")

    # If user is a buyer, redirect
    if (session["role_type"] == "customer"):
        redirect("/")

    data = {
        "seller_id": session["user_id"],
        "product_id": product_id
    }
    # If the product in url not belong to seller, redirect
    if (not Product.check_if_seller_has_product(data)):
        redirect("/")

    # Get product
    product_data = {
        product_id: product_id
    }
    product = Product.get_by_id(product_data)

    return render_template("add_edit_product_form.html", product=product)

@app.route('/delete/product/<int:product_id>')
def delete_product(product_id):
    if (not session):
        redirect("/login_and_register")
    data = {
        "product_id": product_id
    }
    Product.delete(data)
    return redirect('/seller_dashboard')

#####################################
#### This is where the API stays ####
#####################################
@app.route("/api/add_product")
def api_add_product():
    return

@app.route("/api/edit_product")
def api_edit_product():
    return

