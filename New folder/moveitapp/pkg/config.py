
class GeneralConfig(object):
    APP_NAME = 'MoveIt'
    SECRET_KEY = 'notsecured'
    
    
class DevelopmentConfig(GeneralConfig):
    SECRET_KEY = '345bc167807a8eaa0a089dbc36e64e1f4d923a01d4fb3c368c1544017b5a335c'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root@localhost/moveitdb' 
    
    
    