from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.user import User

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