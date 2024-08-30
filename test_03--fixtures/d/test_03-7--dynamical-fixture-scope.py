import cards


def test_empty(cards_db):
    assert cards_db.count() == 0


def test_two(cards_db):
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2


# The fixture scope of "cards_db" is "session"
"""
$ pytest --setup-show -k test_03-7
===================================================================================================== test session starts ======================================================================================================
###                                                                                                                                                                               

test_03d--fixtures/test_03-7--dynamical-fixture-scope.py 
SETUP    S cards_db
        test_03d--fixtures/test_03-7--dynamical-fixture-scope.py::test_empty (fixtures used: cards_db).
        test_03d--fixtures/test_03-7--dynamical-fixture-scope.py::test_two (fixtures used: cards_db).
TEARDOWN S cards_db

=============================================================================================== 2 passed, 32 deselected in 0.04s ===============================================================================================
"""

# The fixture scope of "cards_db" is "function".
# "--func-db" is specified in conftest.py.
"""
$ pytest --func-db --setup-show -k test_03-7
===================================================================================================== test session starts ======================================================================================================
###                                                                                                                                                                              

test_03--fixtures/d/test_03-7--dynamical-fixture-scope.py 
        SETUP    F cards_db
        test_03--fixtures/d/test_03-7--dynamical-fixture-scope.py::test_empty (fixtures used: cards_db).
        TEARDOWN F cards_db
        SETUP    F cards_db
        test_03--fixtures/d/test_03-7--dynamical-fixture-scope.py::test_two (fixtures used: cards_db).
        TEARDOWN F cards_db

=============================================================================================== 2 passed, 32 deselected in 0.04s ===============================================================================================
"""