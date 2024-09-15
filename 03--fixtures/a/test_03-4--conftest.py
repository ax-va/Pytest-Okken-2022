import cards


def test_empty(
        cards_db,  # session fixture determined in conftest.py
):
    assert cards_db.count() == 0


def test_two(
        cards_db,  # session fixture determined in conftest.py
):
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2


# Show the order of tests and fixtures
"""
$ pytest --setup-show 03--fixtures/a/test_03-4--conftest.py
*** test session starts ***
***                                                                                                                                                                           

03--fixtures/a/test_03-4--conftest.py 
SETUP    S cards_db
        03--fixtures/a/test_03-4--conftest.py::test_empty (fixtures used: cards_db).
        03--fixtures/a/test_03-4--conftest.py::test_two (fixtures used: cards_db).
TEARDOWN S cards_db
***
"""
# S in front of the fixture name indicates that the fixture is using session scope

# List fixtures used in a module
"""
$ pytest --fixtures-per-test 03--fixtures/a/test_03-4--contest.py
***
*** fixtures used by test_empty ***
*** (03--fixtures/a/test_03-4--conftest.py:5) ***
cards_db -- 03--fixtures/a/conftest.py:8
    CardsDB object connected to a temporary database 

*** fixtures used by test_two ***
*** (03--fixtures/a/test_03-4--conftest.py:9) ***
cards_db -- 03--fixtures/a/conftest.py:8
    CardsDB object connected to a temporary database 
***
"""

# List fixtures used in a function
"""
$ pytest --fixtures-per-test 03--fixtures/a/test_03-4--conftest.py::test_empty
***
*** fixtures used by test_empty ***
*** (03--fixtures/a/test_03-4--conftest.py:5) ***
cards_db -- 03--fixtures/a/conftest.py:8
    CardsDB object connected to a temporary database
***
"""