# Elder Scrolls: Legends SDK

[![esl-developers on discord](https://img.shields.io/badge/discord-esl--developers-738bd7.svg)](https://discord.gg/97vDaJx)
[![Build Status](https://travis-ci.org/ElderScrollsLegends/elder-scrolls-legends-sdk-python.svg?branch=master)](https://travis-ci.org/ElderScrollsLegends/elder-scrolls-legends-sdk-python)
[![Requirements Status](https://requires.io/github/ElderScrollsLegends/elder-scrolls-legends-sdk-python/requirements.svg?branch=master)](https://requires.io/github/ElderScrollsLegends/elder-scrolls-legends-sdk-python/requirements/?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/ef27076576eb0104d265/maintainability)](https://codeclimate.com/github/ElderScrollsLegends/elder-scrolls-legends-sdk-python/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/ElderScrollsLegends/elder-scrolls-legends-sdk-python/badge.svg?branch=master)](https://coveralls.io/github/ElderScrollsLegends/elder-scrolls-legends-sdk-python?branch=master)

This is the Elder Scrolls: Legends SDK Python implementation. It is a wrapper around the Elder Scrolls: Legends API of [https://elderscrollslegends.io](https://elderscrollslegends.io/).

## Requirements
Python 3 is currently the only supported version for the sdk. More specifically, the package was developed using Python 3.6.

## Installation

Using pip:

    pip install elderscrollslegendssdk

## Usage

Import

    from elderscrollslegendssdk import Card
    from elderscrollslegendssdk import Set
    from elderscrollslegendssdk import Type
    from elderscrollslegendssdk import Keyword
    from elderscrollslegendssdk import Subtype
    from elderscrollslegendssdk import Attribute

### Classes

    Card
    Set
    Type
    Keyword
    Subtype
    Attribute

### Properties Per Class

#### Card

    name
    id
    set
    rarity
    type
    subtypes
    cost
    power
    health
    soul_summon
    soul_trap
    text
    attributes
    keywords
    unique
    collectible
    image_url

#### Set

    id
    name
    total_cards
    release_date

### Functions Available

#### Find a card by id

    card = Card.find('1fd81123ab3eca0b29c4c19757045db9757b4f1a')

#### Filter Cards via query parameters

    cards = Card.where(type='creature', rarity='legendary')
    
#### Find all cards (will take awhile)

    cards = Card.all()
    
#### Get all cards, but only a specific page of data

    cards = Card.where(page=5)
    
#### Find a set by id

    set = Set.find('cs')
    
#### Filter sets via query parameters

    sets = Set.where(name='core')
    
#### Get all Sets

    sets = Set.all()
    
#### Get all Types

    types = Type.all()

#### Get all Subtypes

    subtypes = Subtype.all()

#### Get all Attributes

    attributes = Attribute.all()

#### Get all Keywords

    keywords = Keyword.all()

## Contributing

1. Fork it ( https://github.com/[my-github-username]/elder-scrolls-legends-sdk-python/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## Developing

### Running Tests

    python -m unittest discover -s tests/
