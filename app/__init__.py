from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
from flask_mongoengine import MongoEngine
# import pymongo
# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client.my_word
# from flask_mongokit import MongoKit, Document

# from . import Quizs

db = MongoEngine()

def create_app(config_name):
    app = Flask(__name__)
    #TODO add config
    
    app.debug = True
    # app.config.from_object(DevConfig)
    app.config["MONGODB_SETTINGS"] = {'db': "my_word"}
    app.config["SECRET_KEY"] = "KeepThisS3cr3t"
    db.init_app(app)
    # db.register([Quizs])
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    return app

