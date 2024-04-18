import cards


def test_empty(cards_db):
    assert cards_db.count() == 0


def test_two(cards_db):
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2


# Show the order of tests and fixtures
"""
$ pytest --setup-show -k test_example-03-4
===================================================================================================== test session starts ======================================================================================================
###                                                                                                                                                                           

test_examples-03--fixtures/test_example-03-4--fixtures--conftest.py 
SETUP    S cards_db
        test_examples-03--fixtures/test_example-03-4--fixtures--conftest.py::test_empty (fixtures used: cards_db).
        test_examples-03--fixtures/test_example-03-4--fixtures--conftest.py::test_two (fixtures used: cards_db).
TEARDOWN S cards_db

=============================================================================================== 2 passed, 25 deselected in 0.04s ===============================================================================================
"""
# S in front of the fixture name indicates that the fixture is using session scope

# List fixtures used in a module
"""
$ pytest --fixtures-per-test -k test_example-03-4
###
------------------------------------------------------------------------------------------------- fixtures used by test_empty --------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------- (test_examples-03/test_example-03-4--fixtures--conftest.py:5) ---------------------------------------------------------------------------------
cards_db -- test_examples-03--fixtures/conftest.py:8
    CardsDB object connected to a temporary database 

-------------------------------------------------------------------------------------------------- fixtures used by test_two ---------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------- (test_examples-03/test_example-03-4--fixtures--conftest.py:9) ---------------------------------------------------------------------------------
cards_db -- test_examples-03--fixtures/conftest.py:8
    CardsDB object connected to a temporary database 

==================================================================================================== 25 deselected in 0.03s ====================================================================================================
"""

# List fixtures used in a function
"""
$ pytest --fixtures-per-test test_examples-03--fixtures/test_example-03-4--fixtures--conftest.py::test_empty
###
------------------------------------------------------------------------------------------------- fixtures used by test_empty --------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------- (test_examples-03/test_example-03-4--fixtures--conftest.py:5) ---------------------------------------------------------------------------------
cards_db -- test_examples-03--fixtures/conftest.py:8
    CardsDB object connected to a temporary database 

==================================================================================================== no tests ran in 0.01s =====================================================================================================
"""
