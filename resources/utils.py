# coding: utf-8

from flask_restful import reqparse


def parse_property_arguments():
    parser = reqparse.RequestParser()
    parser.add_argument('x', required=True, type=int)
    parser.add_argument('y', required=True, type=int)
    parser.add_argument('title', required=False, type=unicode)
    parser.add_argument('price', required=False, type=float)
    parser.add_argument('description', required=False, type=unicode)
    parser.add_argument('beds', required=True, type=int)
    parser.add_argument('baths', required=True, type=int)
    parser.add_argument('squareMeters', required=True, type=int)
    parser.add_argument('provinces', required=False)

    return parser.parse_args()
