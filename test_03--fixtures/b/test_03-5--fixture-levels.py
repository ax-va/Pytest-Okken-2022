import cards


def test_empty(cards_db):
    assert cards_db.count() == 0


def test_two(cards_db):
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2


def test_three(cards_db):
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    cards_db.add_card(cards.Card("third"))
    assert cards_db.count() == 3


"""
$ pytest --setup-show test_03--fixtures/b
===================================================================================================== test session starts ======================================================================================================
###
collected 3 items                                                                                                                                                                                                              

test_03--fixtures/b/test_03-5--fixture-levels.py 
SETUP    S db
        SETUP    F cards_db (fixtures used: db)
        test_03--fixtures/b/test_03-5--fixture-levels.py::test_empty (fixtures used: cards_db, db).
        TEARDOWN F cards_db
        SETUP    F cards_db (fixtures used: db)
        test_03--fixtures/b/test_03-5--fixture-levels.py::test_two (fixtures used: cards_db, db).
        TEARDOWN F cards_db
        SETUP    F cards_db (fixtures used: db)
        test_03--fixtures/b/test_03-5--fixture-levels.py::test_three (fixtures used: cards_db, db).
        TEARDOWN F cards_db
TEARDOWN S db

====================================================================================================== 3 passed in 0.04s =======================================================================================================
"""