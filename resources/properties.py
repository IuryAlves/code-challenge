# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint
from flask_restful import Api, Resource
from models.propertie import Propertie
from .utils import parse_property_arguments

blueprint = Blueprint('properties', __name__)
api = Api(blueprint)


@api.resource('/properties', '/properties/<string:id>')
class PropertiesResource(Resource):

    def post(self):
        args = parse_property_arguments()
        Propertie(**args).save()

    def get(self, id):
        user = Propertie.objects.get_or_404(id=id)
        return user.to_dict()
