# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint
from flask_restful import Api, Resource, reqparse, abort

from src.models.propertie import Propertie
from .utils import parse_property_arguments

blueprint = Blueprint('properties', __name__)
api = Api(blueprint)


@api.resource('/properties', '/properties/<string:id>')
class PropertiesResource(Resource):

    def post(self):
        args = parse_property_arguments()
        Propertie(**args).save()
        return {}, 201

    def get(self, id=None):
        parser = reqparse.RequestParser()
        parser.add_argument('ax')
        parser.add_argument('ay')
        parser.add_argument('bx')
        parser.add_argument('by')
        args = parser.parse_args()

        if not all(args.values()) and id is None:
            abort(400, message="You must provide an id or a query string with "
                               "'ax', 'bx', 'ay', 'by")
        if id is not None:
            user = Propertie.objects.get_or_404(id=id)
            return user.to_dict()
        else:
            return Propertie.find_in_area(**args)
