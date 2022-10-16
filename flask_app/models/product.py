from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash

class Product:
    db = 'group6project'
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.quantity = data["quantity"]
        self.size = data["size"]
        self.img = data["img"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.users_id = data["users_id"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM products;"
        results = connectToMySQL(cls.db).query_db(query)
        products = []
        for row in results:
            products.append(cls(row))
        return products

    @classmethod
    def get_all_products_by_seller_id(cls):
        query = "SELECT * FROM products WHERE seller_id = %(seller_id)s;"
        results = connectToMySQL(cls.db).query_db(query)
        products = []
        for row in results:
            products.append(cls(row))
        return products

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM products WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        product = cls(row)
        return product

    @classmethod
    def save(cls,data):
        query = "INSERT INTO products(name,description,instructions,quantity,size,img,users_id) VALUES(%(name)s,%(description)s,%(instructions)s,%(quantity)s,%(size)s,%(img)s,%(users_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM products WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_product(product):
        is_valid = True
        if len(product["name"]) < 2:
            flash("Name must be at least 3 characters")
            is_valid = False
        if len(product["description"]) < 2:
            flash("Description must be at least 3 characters")
            is_valid = False
        if len(product["instructions"]) < 2:
            flash("Instructions must be at least 3 characters")
            is_valid = False
        return is_valid

    @classmethod
    def check_if_seller_has_product(cls, data):
        query = "SELECT * FROM products WHERE product_id = %(product_id)s AND seller_id = %(seller_id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        
        if len(results) < 1:
            return False
        
        return True