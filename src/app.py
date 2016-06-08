# coding: utf-8

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.cors import CORS

app = Flask(__name__)

app.config.from_object('src.settings')

enable_cors = app.config.get("ENABLE_CORS", False)
if enable_cors:
    CORS(app, resources={
        r"/properties/*": {"origins": "*"},
    })

db = MongoEngine(app)

from resources import properties
from models.properties import Property

app.register_blueprint(properties.blueprint)
