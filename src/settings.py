# coding: utf-8

import os


MONGO_HOST = os.getenv("MONGO_HOST", 'localhost')
MONGO_PORT = os.getenv("MONGO_PORT", 27017)
DEBUG = os.getenv("DEBUG", False)
ENABLE_CORS = True
SECRET_KEY = os.getenv("SECRET_KEY")
