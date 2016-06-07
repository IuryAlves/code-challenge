# coding: utf-8

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.cors import CORS

# cria o  app
app = Flask(__name__)

# configura o app a partir do settings
app.config.from_object('settings')

# configura cors
enable_cors = app.config.get("ENABLE_CORS", False)
if enable_cors:
    CORS(app, resources={
        r"/resorce/*": {"origins": "*"},
    })

# configura o banco
db = MongoEngine(app)

from resources import resources

app.register_blueprint(resources.blueprint)
