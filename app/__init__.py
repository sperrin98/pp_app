from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Correct path to config
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints if any
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
