from flask_app.config.mysqlconnection import connectToMySQL


class Order:
    db = 'group6project'
    def __init__( self , data ):
        self.id = data['id']
        self.sub_total = data['sub_total']
        self.tax = data['tax']
        self.total = data['total']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # TODO: get user by id
    # @classmethod
    # def get_user_by_id(cls, data):
        
    # TODO: Create user in db
    # @classmethod
    # def create(cls, data):

            