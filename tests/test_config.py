#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of elderscrollslegendssdk.
# https://github.com/ElderScrollsLegends/elder-scrolls-legends-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Andrew Backes <backes.andrew@gmail.com>

import unittest
from elderscrollslegendssdk import __pypi_packagename__, __github_username__, __github_reponame__, __endpoint__

class TestConfig(unittest.TestCase):
    def test_has_proper_packagename(self):
        self.assertEqual('elderscrollslegendssdk', __pypi_packagename__)
        
    def test_has_proper_github_username(self):
        self.assertEqual('ElderScrollsLegends', __github_username__)
        
    def test_has_proper_github_reponame(self):
        self.assertEqual('elder-scrolls-legends-sdk-python', __github_reponame__)
        
    def test_has_proper_endpoint(self):
        self.assertEqual('https://api.elderscrollslegends.io/v1', __endpoint__)