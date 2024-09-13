"""
Markers can have parameters that can be accessed with .args and .kwargs attributes.
From a fixture, we can access markers using request.node.get_closest_marker(<marker_name>).

We use the marker parameterization to change a fixture:
namely, transform the fixture from database access into a database with any number of entries.
"""

import pytest
from cards import Card

# motivation


@pytest.fixture(scope="function")
def cards_db_zero_cards(cards_db):
    """ Cleans out the database """
    db = cards_db
    db.delete_all()
    return db


@pytest.fixture(scope="function")
def cards_db_three_cards(cards_db):
    """ Cleans out the database and adds three cards """
    db = cards_db
    # Start with empty
    db.delete_all()
    # Add three cards
    db.add_card(Card("Learn something new"))
    db.add_card(Card("Build useful tools"))
    db.add_card(Card("Teach others"))
    return db


def test_zero_card(cards_db_zero_cards):
    assert cards_db_zero_cards.count() == 0


def test_three_card(cards_db_three_cards):
    assert cards_db_three_cards.count() == 3


"""
$ pytest -k test_06-08 -v --disable-warnings
***
test_06-08--marker-parametrization-changing-fixtures.py::test_zero_card PASSED
test_06-08--marker-parametrization-changing-fixtures.py::test_three_card PASSED
***
"""

# Task: How to give the number of cards as parameter


@pytest.fixture(scope="function")
def cards_db_num_cards(cards_db, request, faker):
    db = cards_db
    db.delete_all()
    # Support for "@pytest.mark.num_cards(<some_number>)":
    # Set random seed.
    # Faker provides the faker fixture.
    faker.seed_instance(101)
    # Return a Marker object if the test is marked with num_cards, otherwise it returns None.
    # The term request.node is pytest's representation of a test.
    # get_closest_marker("num_cards") returns the marker closest to
    # the test among functions, methods, classes, and files.
    m = request.node.get_closest_marker("num_cards")
    if m and len(m.args) > 0:
        num_cards = m.args[0]
        for _ in range(num_cards):
            db.add_card(
                Card(
                    summary=faker.sentence(),
                    owner=faker.first_name() + " " + faker.last_name(),
                )
            )
    return db


def test_no_marker(cards_db_num_cards):
    assert cards_db_num_cards.count() == 0


@pytest.mark.num_cards
def test_marker_with_no_param(cards_db_num_cards):
    assert cards_db_num_cards.count() == 0


@pytest.mark.num_cards(3)
def test_three_cards(cards_db_num_cards):
    assert cards_db_num_cards.count() == 3
    # Look at the cards Faker made
    print()
    for card in cards_db_num_cards.list_cards():
        print(card)


@pytest.mark.num_cards(10)
def test_ten_cards(cards_db_num_cards):
    assert cards_db_num_cards.count() == 10


"""
$ pytest -k test_06-08 -v -s --disable-warnings
***
test_06-08--marker-parametrization-changing-fixtures.py::test_zero_card PASSED
test_06-08--marker-parametrization-changing-fixtures.py::test_three_card PASSED
test_06-08--marker-parametrization-changing-fixtures.py::test_no_marker PASSED
test_06-08--marker-parametrization-changing-fixtures.py::test_marker_with_no_param PASSED
test_06-08--marker-parametrization-changing-fixtures.py::test_three_cards 
Card(summary='Suggest training much grow any me own true.', owner='Todd Logan', state='todo', id=1)
Card(summary='Wife audience cover become show hand.', owner='Thomas Nguyen', state='todo', id=2)
Card(summary='Institution as life deep present person.', owner='Mark Trevino', state='todo', id=3)
PASSED
test_06-08--marker-parametrization-changing-fixtures.py::test_ten_cards PASSED
***
"""