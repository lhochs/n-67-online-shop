from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.order import Order
from flask_app.models.payment import Payment

########################################
#### This is where we set the route ####
########################################

# # This route where user can view items he/she added to cart
# @app.route("/cart")
# def cart():
#     return render_template("cart.html")

# # This route where user will confirm their purchase?
# @app.route("/checkout")
# def checkout():
#     # Ngan's note: Need to replace this hardcode data with request.form data
#     # I'm thinking we might have:
#     # - a list of product_id that we captured from front-end
#     # - user_id comes from user login data in session
#     # - total comes from our front-end price calculation
#     data = {
#         'total': 10,
#         'user_id': 1,
#         'products': [
#             {
#                 'product_id': 1,
#                 'quantity': 2
#             }
#         ]
#     }
#     Order.add(data)
#     return render_template("checkout.html")

@app.route("/checkout")
def proceed_to_checkout():
    return render_template("checkout.html")

@app.route("/payment", methods=['POST'])
def make_payment(id):
    if not Payment.validate(request.form):
        return redirect("/checkout")
    data = {
        "credit_num":request.form['credit_num'],
        "billing_address":request.form['billing_address']
    }
    Payment.save(data)
    return redirect("index.html")

#####################################
#### This is where the API stays ####
#####################################
@app.route('/orders/customer_id/order_id', methods=["GET"])
def get_order_for_customer(customer_id):
    # Check if user logs in and user has the same id as given customer_id
    if (not session):
        return {}

    # Only allow user to see his own orders
    if (session["user_id"] != customer_id):
        return {}

    data = {
        order_id: order_id
    }
    order = Order.get_order_by_id(data)

    return render("")