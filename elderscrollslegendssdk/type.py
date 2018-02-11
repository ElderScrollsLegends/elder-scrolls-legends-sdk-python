#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of elderscrollslegendssdk.
# https://github.com/ElderScrollsLegends/elder-scrolls-legends-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Andrew Backes <backes.andrew@gmail.com>

from elderscrollslegendssdk.querybuilder import QueryBuilder

class Type(object):
    RESOURCE = 'types'

    @staticmethod
    def all():
        return QueryBuilder(Type).array()