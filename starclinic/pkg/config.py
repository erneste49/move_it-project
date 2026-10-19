import os
from dotenv import load_dotenv

load_dotenv()


class GeneralConfig:
    APP_NAME = 'star_clinic'
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(GeneralConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = '587'
    MAIL_USERNAME = 'roiernest01@gmail.com'
    MAIL_PASSWORD = 'hshltpvcyasfgoaj'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False 
    MAIL_DEFAULT_SENDER = 'roiernest01@gmail.com'
    
    