#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of elderscrollslegendssdk.
# https://github.com/ElderScrollsLegends/elder-scrolls-legends-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import unittest
from elderscrollslegendssdk import ElderScrollsLegendsException

class TestElderScrollsLegendsException(unittest.TestCase):
    def test_constructor_sets_description(self):
        description = "An error has occurred"
        exception = ElderScrollsLegendsException(description)
        
        self.assertEqual(description, exception.__str__())