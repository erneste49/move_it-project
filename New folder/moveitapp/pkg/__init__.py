from flask import Flask
from flask_migrate import Migrate
from pkg.config import DevelopmentConfig
from pkg.home.routes import home 
from pkg.users.routes import user



def create_app():
    from pkg.models import db
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    
    
    app.register_blueprint(home)
    app.register_blueprint(user)
    
    db.init_app(app)
    migrate = Migrate(app, db)
    
    return app

app = create_app()

