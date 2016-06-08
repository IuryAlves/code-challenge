# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from models.propertie import Propertie
from .utils import parse_property_arguments

blueprint = Blueprint('properties', __name__)
api = Api(blueprint)


@api.resource('/properties', '/properties/<string:id>')
class PropertiesResource(Resource):

    def post(self):
        args = parse_property_arguments()
        Propertie(**args).save()

    def get(self, id=None):
        if id is not None:
            user = Propertie.objects.get_or_404(id=id)
            return user.to_dict()
        else:
            parser = reqparse.RequestParser()
            parser.add_argument('ax', required=True)
            parser.add_argument('ay', required=True)
            parser.add_argument('bx', required=True)
            parser.add_argument('by', required=True)
            args = parser.parse_args()

            return Propertie.find_in_area(**args)
