#!/usr/bin/env python
# coding: utf-8

from __future__ import (
    print_function,
    unicode_literals,
    absolute_import
)

import argparse
import json
import os


def get_path():
    return unicode(os.path.abspath('.'))


def parse_args():
    _parser = argparse.ArgumentParser()
    _parser.add_argument('--fixture', type=str, help='fixture file to load', default='properties.json')
    _parser.add_argument('--fixture_folder', type=str,
                         default='models/fixtures',
                         help='where fixtures are stored.'
                         )
    return _parser.parse_args()

def main(base_path):
    properties_to_save = []
    args = parse_args()
    path = os.path.sep.join([base_path,
                             'app',
                             args.fixture_folder,
                             args.fixture])
    with open(path) as file_:
        data = json.load(file_)
    properties = data['properties']
    for property_ in properties:
        property_.pop('id')
        properties_to_save.append(Property(**property_))
    Property.objects.insert(properties_to_save)

    return len(properties_to_save)


if __name__ == '__main__':
    from app.models.properties import Property
    base_path = get_path()
    out = main(base_path)
    print("{} objects saved".format(out))