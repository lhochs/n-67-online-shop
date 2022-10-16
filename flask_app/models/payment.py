from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash

class Payment:
    db = 'group6project'

    def __init__(self,data):
        self.payment_id = data["payment_id"]
        self.credit_num = data["credit_num"]
        self.billing_address = data["billing_address"]

    @classmethod
    def get_payment_by_id(cls, data):
        query = """
            SELECT payment_id, credit_num, billing_address, created_at, updated_at
            FROM payments 
            WHERE payment_id = %(payment_id)s
        """
        results = connectToMySQL(cls.db).query_db(query)

        payment = cls(result[0])
        
        return payment