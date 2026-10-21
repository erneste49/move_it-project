import os

class GeneralConfig(object):
    APP_NAME = 'MoveIt'
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    
    
class DevelopmentConfig(GeneralConfig):
    
   SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
   PAYSTACK_SECRET_KEY = os.getenv('PAYSTACK_API_SECRET_KEY') 
   
    
    
    