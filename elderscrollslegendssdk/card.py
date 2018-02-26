#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of elderscrollslegendssdk.
# https://github.com/ElderScrollsLegends/elder-scrolls-legends-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Andrew Backes <backes.andrew@gmail.com>

import json
from elderscrollslegendssdk.querybuilder import QueryBuilder

class Card(object):
    RESOURCE = 'cards'

    def __init__(self, response_dict={}):
        Object = lambda **kwargs: type("Object", (), kwargs)
        self.name = response_dict.get('name')
        self.id = response_dict.get('id')
        self.set = Object(id=response_dict.get('set')['id'], name=response_dict.get('set')['name'])
        self.rarity = response_dict.get('rarity')
        self.type = response_dict.get('type')
        self.subtypes = response_dict.get('subtypes')
        self.cost = response_dict.get('cost')
        self.power = response_dict.get('power')
        self.health = response_dict.get('health')
        self.soul_summon = response_dict.get('soulSummon')
        self.soul_trap = response_dict.get('soulTrap')
        self.text = response_dict.get('text')
        self.attributes = response_dict.get('attributes')
        self.keywords = response_dict.get('keywords')
        self.unique = response_dict.get('unique')
        self.image_url = response_dict.get('imageUrl')

    @staticmethod
    def find(id):
        return QueryBuilder(Card).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(Card).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(Card).all()
