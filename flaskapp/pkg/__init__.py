import os
from flask import Flask
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect   
from pkg import config  
from flask_migrate import Migrate 


load_dotenv()

csrf = CSRFProtect()      #Global csrf protection

def create_app():
    from pkg.models import db
    app = Flask(__name__, static_folder="static")

    #app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)
    
    migrate = Migrate(app, db)
    
    csrf.init_app(app)
    
    return app

app = create_app()
   


from pkg import forms,  user_routes, admin_routes , orm_routes






##print(app.config)