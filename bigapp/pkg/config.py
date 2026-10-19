
class GeneralConfig(object):
    APP_NAME='BigApp'
    SECRET_KEY = 'notsecured'
    
    
class DevelopmentConfig(GeneralConfig):
    SECRET_KEY='88fa5fad3dfb7999bc2dc194ed7d88cb519f5457bcc9f2fcefcf02996935459e'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root@localhost/bigappdb' 
    
    
    