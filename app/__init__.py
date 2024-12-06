from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Debug print the database URI
    print(f"SQLALCHEMY_DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

    db.init_app(app)

    # Enable CORS for all routes
    CORS(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
