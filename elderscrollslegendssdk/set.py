#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of elderscrollslegendssdk.
# https://github.com/ElderScrollsLegends/elder-scrolls-legends-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Andrew Backes <backes.andrew@gmail.com>

import json
from elderscrollslegendssdk.querybuilder import QueryBuilder

class Set(object):
    RESOURCE = 'sets'

    def __init__(self, response_dict={}):
        self.name = response_dict.get('name')
        self.id = response_dict.get('id')
        self.total_cards = response_dict.get('totalCards')
        self.release_date = response_dict.get('releaseDate')

    @staticmethod
    def find(id):
        return QueryBuilder(Set).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(Set).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(Set).all()
