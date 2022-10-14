from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/signup")
def signup():
  return render_template("signup.html")

# This route can be used for both seller and buyer, based on user role
@app.route("/user/dashboard")
def dashboard():
  return render_template("dashboard.html")

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

if __name__ == "__main__":
  app.run(debug=True)