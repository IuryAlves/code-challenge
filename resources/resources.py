# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint
from flask_restful import Api, Resource


blueprint = Blueprint('resource', __name__)
api = Api(blueprint)


@api.resource('/resource/')
class _Resource(Resource):

    def get(self):
        return {}
