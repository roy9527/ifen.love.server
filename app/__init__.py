from flask import Flask
# from config import config

def create_app(config_name):
    app = Flask(__name__)
    #TODO add config

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    return app