# coding: utf-8

from __future__ import (
    absolute_import,
    print_function,
    unicode_literals
)

from mongoengine import DoesNotExist

from src.models.propertie import Propertie
from src.exceptions import ValidationError


class Province(object):

    def __init__(self, point1, point2):
        self.ax, self.ay = point1
        self.bx, self.by = point2

    def __repr__(self):
        return '{cls}(({p1}, {p2}), ({p3}, {p4}))'.format(
            cls=self.__class__.__name__,
            p1=self.ax,
            p2=self.bx,
            p3=self.ay,
            p4=self.by
        )

gode = Province((0, 1000),
                (600, 500))
ruja = Province((400, 1000),
                (1110, 500))

provinces = (
    gode,
    ruja
)


def get_property(id):
    try:
        property = Propertie.objects.get(pk=id)
    except DoesNotExist:
        return None
    else:
        return property


def find_by_area(**kwargs):
    return Propertie.find_in_area(**kwargs)


def save_property(**kwargs):
    x = kwargs.get("x")
    y = kwargs.get("y")
    beds = kwargs.get("beds")
    baths = kwargs.get("baths")
    square_meters = kwargs.get("squareMeters")

    if x < 0 or x > 1400:
        raise ValidationError(
            'x value cannot be lower than zero or greater than 1400.'
            'x is {}'.format(x)
        )
    elif y < 0 or y > 1000:
        raise ValidationError(
            'y value cannot be lower than zero or greater than 1000.'
            'y is {}'.format(y)
        )

    elif beds > 5 or beds < 1:
        raise ValidationError(
            'The number of beds cannot be lower than 1 or greater than 5'
        )
    elif baths > 4 or baths < 1:
        raise ValidationError(
            'The number of baths cannot be lower than 1 or greater than 4'
        )

    elif square_meters > 240 or square_meters < 20:
        raise ValidationError(
            'squareMeters cannot be greater than 240 or lower than 20.'
        )
    property = Propertie(**kwargs).save()
