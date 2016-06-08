# coding: utf-8

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.cors import CORS
from flask.ext.cache import Cache


app = Flask(__name__)
app.config.from_object('src.settings')

enable_cors = app.config.get("ENABLE_CORS", False)
if enable_cors:
    CORS(app, resources={
        r"/properties/*": {"origins": "*"},
    })

db = MongoEngine(app)
cache = Cache(config={"CACHE": app.config.get("CACHE_TYPE")})
cache.init_app(app)

from resources import properties

app.register_blueprint(properties.blueprint)
