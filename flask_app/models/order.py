from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.product import Product
import json

class Order:
    db = 'group6project'
    def __init__( self , data ):
        self.id = data['id']
        self.total = data['total']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_orders_by_user_id(cls, data):
        query = "SELECT * FROM orders WHERE user_id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query)

        orders = []
        for row in results:
            orders.append(cls(row))
        return orders
        
    @classmethod
    def add(cls, data):
        order_data = {
            'total': data['total'],
            'user_id': data['user_id']
        }
        # add order
        query = "INSERT INTO orders(total, user_id) VALUES (%(total)s, %(user_id)s);"
        order_id = connectToMySQL(cls.db).query_db(query, order_data)

        # add products associated with order
        products = data['products']
        for product in products:
            orders_products_data = {
                'order_id': order_id,
                'product_id': product['product_id'],
                'quantity': product['quantity']
            }

            query = "INSERT INTO orders_products(order_id, product_id, quantity) VALUES (%(order_id)s, %(product_id)s, %(quantity)s);"
            connectToMySQL(cls.db).query_db(query, orders_products_data)

            # update product quantity after purchase complete
            product_data = {
                'quantity': product['quantity'],
                'product_id': product['product_id'],
            }
            query = "UPDATE products SET quantity = quantity - %(quantity)s WHERE id = %(product_id)s LIMIT 1;"
            connectToMySQL(cls.db).query_db(query, product_data)
        

        return order_id
