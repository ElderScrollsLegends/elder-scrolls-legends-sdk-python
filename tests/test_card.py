#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of elderscrollslegendssdk.
# https://github.com/ElderScrollsLegends/elder-scrolls-legends-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Andrew Backes <backes.andrew@gmail.com>

import unittest
import vcr
from elderscrollslegendssdk import Card

# Python 3.6 Workaround until https://github.com/kevin1024/vcrpy/issues/293 is fixed.
vcr_connection_request = vcr.stubs.VCRConnection.request 
vcr.stubs.VCRConnection.request = lambda *args, **kwargs: vcr_connection_request(*args)

class TestCard(unittest.TestCase):
    def test_find_returns_card(self):
        with vcr.use_cassette('fixtures/alduin.yaml'):
            card = Card.find('1fd81123ab3eca0b29c4c19757045db9757b4f1a')

            self.assertEqual('Alduin', card.name)
            self.assertEqual('1fd81123ab3eca0b29c4c19757045db9757b4f1a', card.id)
            self.assertEqual('Heroes of Skyrim', card.set.name)
            self.assertEqual('hos', card.set.id)
            self.assertEqual('Legendary', card.rarity)
            self.assertEqual('Creature', card.type)
            self.assertEqual('Dragon', card.subtype)
            self.assertEqual(20, card.cost)
            self.assertEqual(12, card.power)
            self.assertEqual(12, card.health)
            self.assertEqual(1200, card.soul_summon)
            self.assertEqual(400, card.soul_trap)
            self.assertEqual('Costs 2 less for each Dragon in your discard pile. Summon: Destroy all other creatures. At the start of your turn, summon a random Dragon from your discard pile.', card.text)
            self.assertEqual(['Neutral'], card.attributes)
            self.assertEqual([], card.keywords)
            self.assertTrue(card.unique)
            self.assertEqual('https://images.elderscrollslegends.io/hos/alduin.png', card.image_url)

    def test_all_with_params_return_cards(self):
        with vcr.use_cassette('fixtures/legendary_creatures.yaml'):
            cards = Card.where(rarity='legendary', type='creature')
            self.assertTrue(len(cards) >= 80)

    def test_all_with_page_returns_cards(self):
        with vcr.use_cassette('fixtures/all_first_page.yaml'):
            cards = Card.where(page=1)
            self.assertEqual(100, len(cards))

    def test_all_with_page_and_page_size_returns_card(self):
        with vcr.use_cassette('fixtures/all_first_page_one_card.yaml'):
            cards = Card.where(page=1, pageSize=1)
            self.assertEqual(1, len(cards))
