# coding: utf-8

from __future__ import (
    print_function,
    unicode_literals,
    absolute_import
)


class Province(object):

    def __init__(self, point1, point2):
        self.ax, self.ay = point1
        self.bx, self.by = point2

    def __repr__(self):
        return '{cls}'.format(
            cls=self.__class__.__name__,
        )


class Gode(Province):

    def __init__(self):
        super(Gode, self).__init__(
            (0, 1000), (600, 500)
        )


class Ruja(Province):

    def __init__(self):
        super(Ruja, self).__init__(
            (400, 1000),
            (1110, 500)
        )


class Jaby(Province):

    def __init__(self):
        super(Jaby, self).__init__(
            (1100, 1000),
            (1400, 500)
        )


class Scavy(Province):

    def __init__(self):
        super(Scavy, self).__init__(
            (0, 500),
            (600, 0)
        )


class Groola(Province):

    def __init__(self):
        super(Groola, self).__init__(
            (600, 500),
            (800, 0)
        )


class Nova(Province):

    def __init__(self):
        super(Nova, self).__init__(
            (800, 500),
            (1400, 0)
        )

provinces = (
    Gode(),
    Ruja(),
    Jaby(),
    Scavy(),
    Groola(),
    Nova()
)


def find_provinces(x, y):
    """
    >>> list(find_provinces(999, 333))
    ['Nova']
    >>> list(find_provinces(870, 867))
    ['Ruja']
    """
    for province in provinces:
        if (x > province.ax and
            x < province.bx and
            y > province.by and
            y < province.ay):
            yield repr(province)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
