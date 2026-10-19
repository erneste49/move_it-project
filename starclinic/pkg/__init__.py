from flask import Flask
from flask_migrate import Migrate
from pkg.config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
import os
from flask_mail import Mail 
    
csrf = CSRFProtect()
mail = Mail()


def create_app():
    from pkg.models import db
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.config 
    
    db.init_app(app)
    
    migrate=Migrate(app,db)
    
    csrf.init_app(app)
    mail.init_app(app)
    
    
    return app


app = create_app()

from pkg import routes