from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from .config import Config

db = SQLAlchemy()
api = Api(title='Team & Role API', version='1.0', description='Manage Teams and Roles')

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from .routes import ns
    api.init_app(app)
    api.add_namespace(ns)
    return app
