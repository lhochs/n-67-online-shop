from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.product import Product

########################################
#### This is where we set the route ####
########################################
# This is where user can add product
@app.route("/user/add_product")
def add_product():
    if (not session):
        return redirect("/login_and_register")

    # If user is a customer, redirect
    if (session["role_type"] == "customer"):
        return redirect("/")

    return render_template("add_edit_product_form.html")

# This is where user can edit product
@app.route("/user/edit_product/<product_id>")
def edit_product(product_id):
    # If user is not logged in, redirect
    if (not session):
        return redirect("/login_and_register")

    # If user is a customer, redirect
    if (session["role_type"] == "customer"):
        return redirect("/")

    data = {
        "seller_id": session["user_id"],
        "product_id": product_id
    }
    # If the product in url not belong to seller, redirect
    if (not Product.check_if_seller_has_product(data)):
        return redirect("/")

    # Get product
    product_data = {
        product_id: product_id
    }
    product = Product.get_by_id(product_data)

    return render_template("add_edit_product_form.html", product=product)

@app.route("/dashboard_seller")
def dashboard_seller():
    user_id = session["user_id"]
    data = {
        "seller_id": user_id
    }
    all_products = Product.get_all_products_with_users(data)

    return render_template("dashboard_seller.html", all_products = all_products, user_id = user_id)

#####################################
#### This is where the API stays ####
#####################################
@app.route("/api/add_product")
def api_add_product():
    return

@app.route("/api/edit_product")
def api_edit_product():
    return
