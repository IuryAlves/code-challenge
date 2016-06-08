# coding: utf-8

from __future__ import (
    absolute_import,
    print_function,
    unicode_literals
)

from mongoengine import DoesNotExist
from raise_if import raise_if

from src.models.properties import Property
from src.exceptions import ValidationError
from .provinces import find_provinces


def include_provinces(x, y):
    return list(find_provinces(x, y))


def get_property(id):
    try:
        property_ = Property.objects.get(pk=id)
    except DoesNotExist:
        return None
    else:
        provinces = include_provinces(property_.x, property_.y)
        dic = property_.to_dict()
        dic['provinces'] = provinces
        return dic


def find_by_area(**kwargs):
    for property_ in Property.find_in_area(**kwargs):
        dic = property_.to_dict()
        dic['provinces'] = include_provinces(property_.x, property_.y)
        yield dic


def save_property(**kwargs):
    x = kwargs.get("x")
    y = kwargs.get("y")
    beds = kwargs.get("beds")
    baths = kwargs.get("baths")
    square_meters = kwargs.get("squareMeters")

    raise_if(x < 0 or x > 1400,
             ValidationError,
             'x value cannot be lower than zero or greater than 1400.'
             'x is {}'.format(x)
             )
    raise_if(y < 0 or y > 1000,
             ValidationError,
             'y value cannot be lower than zero or greater than 1000.'
             'y is {}'.format(y)
             )

    raise_if(beds > 5 or beds < 1,
             ValidationError,
             'The number of beds cannot be lower than 1 or greater than 5'
             )
    raise_if(baths > 4 or baths < 1,
             ValidationError,
             'The number of baths cannot be lower than 1 or greater than 4'
             )

    raise_if(square_meters > 240 or square_meters < 20,
             ValidationError,
             'squareMeters cannot be greater than 240 or lower than 20.'
             )
    return Property(**kwargs).save()
