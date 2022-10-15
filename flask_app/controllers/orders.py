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
    # Ngan's note: Need to replace this hardcode data with request.form data
    # I'm thinking we might have:
    # - a list of product_id that we captured from front-end
    # - user_id comes from user login data in session
    # - total comes from our front-end price calculation
    data = {
        'total': 10,
        'user_id': 1,
        'products': [
            {
                'product_id': 1,
                'quantity': 2
            }
        ]
    }
    Order.add(data)
    return render_template("checkout.html")