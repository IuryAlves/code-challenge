# coding: utf-8

from __future__ import (
    print_function,
    unicode_literals,
    absolute_import
)

import flask_restful
from src.decorators import on_exception


class Resource(flask_restful.Resource):

    method_decorators = [on_exception]
