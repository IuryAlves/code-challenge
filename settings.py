# coding: utf-8

import os


MONGO_HOST = 'localhost'
MONGO_PORT = 27017
DEBUG = True
ENABLE_CORS = True
SECRET_KEY = os.getenv("SECRET_KEY")
