

class GeneralConfig(object):
    APP_NAME = 'Flask App'
    ADMIN_EMAIL = 'admin@example.com'
    SECRET_KEY = 'weaksecretkey'
    
    
    
class DevelopmentConfig(GeneralConfig):
    SECRET_KEY = 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root@localhost/devdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
    