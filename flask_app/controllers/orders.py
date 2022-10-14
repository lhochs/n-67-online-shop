from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.order import Order

# This route where user can view items he/she added to cart
@app.route("/cart")
def cart():
    return render_template("cart.html")

# This route where user will confirm their purchase?
@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

# This is where user can add product
@app.route("/user/add_product")
def add_product():
    return render_template("add_edit_product_form.html")

# This is where user can edit product
@app.route("/user/edit_product/<id>")
def edit_product(id):
    return render_template("add_edit_product_form.html")