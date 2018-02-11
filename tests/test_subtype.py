#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of elderscrollslegendssdk.
# https://github.com/ElderScrollsLegends/elder-scrolls-legends-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Andrew Backes <backes.andrew@gmail.com>

import vcr
import unittest
from elderscrollslegendssdk import Subtype

class TestSubtype(unittest.TestCase):
    def test_all_returns_subtypes(self):
        with vcr.use_cassette('fixtures/subtypes.yaml'):
            subtypes = Subtype.all()
            self.assertTrue(len(subtypes) >= 25)
            self.assertTrue('Argonian' in subtypes)