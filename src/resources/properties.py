# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint
from flask_restful import Api, reqparse, abort

from src.usecase import spotippos
from src.resources import Resource
from .utils import parse_property_arguments

blueprint = Blueprint('properties', __name__)
api = Api(blueprint)


@api.resource('/properties', '/properties/<string:id>')
class PropertiesResource(Resource):

    def post(self):
        args = parse_property_arguments()
        spotippos.save_property(**args)
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
            property = spotippos.get_property(id)
            if property is None:
                abort(404)
            else:
                return property.to_dict()
        else:
            properties = spotippos.find_by_area(**args)
            return {
                "foundProperties": len(properties),
                "properties": [
                    property.to_dict() for property in properties
                ]
            }
