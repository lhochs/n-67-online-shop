from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash

class Product:
    db = 'group6project'
    def __init__(self,data):
        self.product_id = data['product_id']
        self.product_name = data['product_name']
        self.price_per_unit = data['price_per_unit']
        self.product_description = data['product_description']
        self.product_qauntity = data['product_qauntity']
        self.product_img = data['product_img']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.seller_id = data['seller_id']
        self.users = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM products;"
        results = connectToMySQL(cls.db).query_db(query)
        products = []
        for row in results:
            products.append(cls(row))
        return products

    @classmethod
    def get_all_products_by_seller_id(cls, data):
        query = "SELECT * FROM products WHERE seller_id = %(seller_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
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
        query = "INSERT INTO products(product_name,price_per_unit,product_description,product_instructions,product_quantity,product_img,seller_id) VALUES(%(product_name)s,%(price_per_unit)s,%(product_description)s,%(product_instructions)s,%(product_quantity)s,%(product_img)s,%(seller_id)s);"
        print (connectToMySQL(cls.db).query_db(query,data))

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
    def get_all_products_with_users(cls, data):
        query = "SELECT * FROM products JOIN users ON products.seller_id = users.user_id WHERE seller_id=%(seller_id)s;"
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        if len(results) < 1:
            return []
        all_products = []
        for row in results:
            product = cls(row)
            i = {
                "user_id":row["user_id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"],
                "email" : row['email'],
                "password" : row['password'],
                "role_type" : row['role_type'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            product.users = User(i)
            all_products.append(product)
        return all_products

    @classmethod
    def check_if_seller_has_product(cls, data):
        query = "SELECT * FROM products WHERE product_id = %(product_id)s AND seller_id = %(seller_id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        
        if len(results) < 1:
            return False
        
        return True