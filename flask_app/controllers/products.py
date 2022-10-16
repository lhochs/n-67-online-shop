from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.product import Product


# This is where user can add product
@app.route("/user/add_product")
def add_product():
    return render_template("add_form.html")

# This is where user can edit product
@app.route("/user/edit_product/<id>")
def edit_product(id):
    return render_template("edit_form.html")