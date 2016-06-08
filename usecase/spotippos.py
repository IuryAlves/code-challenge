# coding: utf-8

from __future__ import (
    absolute_import,
    print_function,
    unicode_literals
)


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
