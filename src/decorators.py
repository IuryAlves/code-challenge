# coding: utf-8

from __future__ import (
    print_function,
    unicode_literals,
    absolute_import
)

from contextlib import wraps
from flask_restful import abort
from src.exceptions import ValidationError


def on_exception(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if isinstance(e, ValidationError):
                return abort(422, message=str(e))
            raise e
    return wrapper
