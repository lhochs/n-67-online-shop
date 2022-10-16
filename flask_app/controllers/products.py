from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.product import Product, User


# This is where user can add product
@app.route("/user/add_product")
def add_product():
    return render_template("add_edit_product_form.html")

# This is where user can edit product
@app.route("/user/edit_product/<id>")
def edit_product(id):
    return render_template("add_edit_product_form.html")

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
    