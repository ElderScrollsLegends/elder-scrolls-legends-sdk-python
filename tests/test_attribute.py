#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of elderscrollslegendssdk.
# https://github.com/ElderScrollsLegends/elder-scrolls-legends-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import vcr
import unittest
from elderscrollslegendssdk import Attribute

class TestAttribute(unittest.TestCase):
    def test_all_returns_attributes(self):
        with vcr.use_cassette('fixtures/attributes.yaml'):
            attributes = Attribute.all()
            self.assertTrue(len(attributes) >= 6)
            self.assertTrue('Strength' in attributes)