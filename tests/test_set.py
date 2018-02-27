#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of elderscrollslegendssdk.
# https://github.com/ElderScrollsLegends/elder-scrolls-legends-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Andrew Backes <backes.andrew@gmail.com>

import vcr
import unittest
from elderscrollslegendssdk import Set

class TestSet(unittest.TestCase):
    def test_find_returns_set(self):
        with vcr.use_cassette('fixtures/cs.yaml'):
            set = Set.find('cs')
            
            self.assertEqual('cs', set.id)
            self.assertEqual('Core Set', set.name)
            self.assertEqual(444, set.total_cards)
            self.assertEqual('2016-04-01', set.release_date)
            
    def test_where_filters_on_name(self):
        with vcr.use_cassette('fixtures/filtered_sets.yaml'):
            sets = Set.where(name='core')
            
            self.assertEqual(1, len(sets))
            self.assertEqual('cs', sets[0].id)
            
    def test_all_returns_all_sets(self):
        with vcr.use_cassette('fixtures/all_sets.yaml'):
            sets = Set.all()

            self.assertGreater(len(sets), 5)
