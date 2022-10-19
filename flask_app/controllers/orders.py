from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.order import Order
from flask_app.models.product import Product
from flask_app.models.user import User


########################################
#### This is where we set the route ####
########################################
# This route where user can view items he/she added to cart
@app.route("/cart")
def cart():

    tax_percent = 0.09375 #hard-code
    cart={}
    sub_total = 0.00
    tax_amount = 0
    shipping_cost = 8.00
    total = 0

    if "cart" in session:
        cart = session["cart"]
        sub_total = 0.00
        total = 0

        for product_id in cart:
            sub_total += round(cart[product_id]["price_per_unit"] * cart[product_id]["quantity"], 2)
        sub_total = round(sub_total, 2)
        shipping_cost = 8.00
        tax_amount = round(sub_total*tax_percent, 2)
        total = sub_total + tax_amount + shipping_cost
    
    return render_template("cart.html", cart=cart, sub_total=sub_total, total=total, shipping_cost = shipping_cost, tax_amount=tax_amount)

@app.route('/cart/add', methods=['POST'])
def addToCart():
    if 'user_id' not in session:
        return {
            "error": "Not logged in"
        }

    product_id = request.json["product_id"]
    product_name = request.json["product_name"]
    price_per_unit = request.json["price_per_unit"]
    product_img = request.json["product_img"]

    product = {
        "product_img": product_img,
        "product_name": product_name,
        "price_per_unit": price_per_unit,
        "quantity": 1
    }

    # Add product to cart in session
    if 'cart' not in session:
        session["cart"] = {}
        session["cart"][product_id] = product
    else:
        cart = session['cart']
        if product_id in cart:
            cart[product_id]["quantity"] += 1
        else:
            cart[product_id] = product
        session['cart'] = cart
    
    return {
        "success": True
    }


# # This route where user will confirm their purchase?
# @app.route("/checkout")
# def checkout():
#     # Ngan's note: Need to replace this hardcode data with request.form data
#     # I'm thinking we might have:
#     # - a list of product_id that we captured from front-end
#     # - user_id comes from user login data in session
#     # - total comes from our front-end price calculation
#     data = {
#         "customer_id": session["user_id"],
#         "product_id": id
#     }

#     product = Product.get_by_id(data)
#     return redirect("/", product = product)

# # # This route where user can view items he/she added to cart
# # @app.route("/cart")
# # def cart():
# #     return render_template("cart.html")

# # # This route where user will confirm their purchase?
# # @app.route("/checkout")
# # def checkout():
# #     # Ngan's note: Need to replace this hardcode data with request.form data
# #     # I'm thinking we might have:
# #     # - a list of product_id that we captured from front-end
# #     # - user_id comes from user login data in session
# #     # - total comes from our front-end price calculation
# #     data = {
# #         'total': 10,
# #         'user_id': 1,
# #         'products': [
# #             {
# #                 'product_id': 1,
# #                 'quantity': 2
# #             }
# #         ]
# #     }
# #     Order.add(data)
# #     return render_template("checkout.html")


# # @app.route('/checkout')
# # def proceed_to_checkout():
# #     return render_template('checkout.html')

# # @app.route('/payment', methods=['POST'])
# # def make_payment():
# #     if not Payment.validate(request.form):
# #         return redirect('/checkout/new')
# #     data = {
# #         "credit_num":request.form["credit_num"],
# #         "billing_address":request.form["billing_address"]
# #     }
# #     Payment.save(data)
# #     return redirect('/')

@app.route("/clear_cart", methods=["GET"])
def clear_cart():
    if "cart" in session:
        # cart = session["cart"]
        # print(session["cart"])
        session.pop("cart")
    return redirect("/")


#####################################
#### This is where the API stays ####
#####################################
@app.route("/clear_cart", methods=["GET"])
def clear_cart():
    session.pop("cart")
    return redirect("/cart")

@app.route('/orders/customer_id/order_id', methods=["GET"])
def get_order_for_customer(customer_id, order_id):
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

    return render_template("order_detail.html", order=order)

@app.route("/submit_checkout", methods=["POST"])
def submit_checkout():
    data = {
        "address": request.form["address"],
        "sub_total": request.form["sub_total"],
        "taxes": request.form["taxes"],
        "shipping": request.form["shipping"],
        "grand_total": request.form["grand_total"],
        "customer_id": session["user_id"],
        "products": request.form["products"]
    }
    new_order = Order.add(data)

    return redirect("/customer_dashboard/" + new_order)

