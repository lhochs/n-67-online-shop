from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.payment import Payment

@app.route('/checkout')
def proceed_to_checkout():
    return render_template('checkout.html')

@app.route('/payment', methods=['POST'])
def make_payment():
    if not Payment.validate(request.form):
        return redirect('/checkout')
    data = {
        "credit_num":request.form["credit_num"],
        "billing_address":request.form["billing_address"]
    }
    Payment.save(data)
    return redirect('/')