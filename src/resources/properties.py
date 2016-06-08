# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint
from flask_restful import Api, reqparse, abort
from mongoengine import DoesNotExist, ValidationError

from src.app import cache
from src.usecase import spotippos
from src.resources import Resource
from .utils import parse_property_arguments

blueprint = Blueprint('properties', __name__)
api = Api(blueprint)


@api.resource('/properties', '/properties/', '/properties/<string:id>')
class PropertiesResource(Resource):

    def delete(self, id=None):
        if id is None:
            abort(400, message="You must provide an id")
        try:
            property_ = spotippos.get_property(id, as_dict=False)
        except (DoesNotExist, ValidationError):
            return {
                "message": 'property with id {id} does not exist.'.format(id=id)
            }, 404
        else:
            property_.delete()
            return {}, 204

    def post(self):
        args = parse_property_arguments()
        property_ = spotippos.save_property(**args)
        return spotippos.get_property(property_.id), 201

    @cache.memoize(timeout=100)
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
            property_dic = spotippos.get_property(id)
            if property_dic is None:
                abort(404, message="property with id {} not found.".format(id))
            else:
                return property_dic
        else:
            properties = list(spotippos.find_by_area(**args))
            return {
                "foundProperties": len(properties),
                "properties": properties
            }
