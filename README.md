# Elder Scrolls: Legends SDK

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
    subtype
    cost
    power
    health
    soul_summon
    soul_trap
    text
    attributes
    keywords
    unique
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
