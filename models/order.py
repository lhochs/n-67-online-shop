from config.mysqlconnection import connectToMySQL

DB = 'group6project'

# Note from Ngan: this is the initial fields that I put for now, 
# we can update as we go
class Order:
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

            