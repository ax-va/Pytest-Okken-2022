import cards


def test_empty(cards_db_empty):
    assert cards_db_empty.count() == 0


def test_two(cards_db_empty):
    db = cards_db_empty
    db.add_card(cards.Card("first"))
    db.add_card(cards.Card("second"))
    assert db.count() == 2


def test_three(cards_db_empty):
    db = cards_db_empty
    db.add_card(cards.Card("first"))
    db.add_card(cards.Card("second"))
    db.add_card(cards.Card("third"))
    assert db.count() == 3


"""
$ pytest --setup-show 03--fixtures/b
===================================================================================================== test session starts ======================================================================================================
###
collected 3 items                                                                                                                                                                                                              

03--fixtures/b/test_03-5--fixture-levels.py
###
SETUP    S cards_db
        SETUP    F cards_db_empty (fixtures used: cards_db)
        03--fixtures/b/test_03-5--fixture-levels.py::test_empty (fixtures used: cards_db_empty, cards_db, ###).
        TEARDOWN F cards_db_empty
        SETUP    F cards_db_empty (fixtures used: cards_db)
        03--fixtures/b/test_03-5--fixture-levels.py::test_two (fixtures used: cards_db_empty, cards_db, ###).
        TEARDOWN F cards_db_empty
        SETUP    F cards_db_empty (fixtures used: cards_db)
        03--fixtures/b/test_03-5--fixture-levels.py::test_three (fixtures used: cards_db_empty, cards_db, ###).
        TEARDOWN F cards_db_empty
TEARDOWN S cards_db
###
====================================================================================================== 3 passed in 0.04s =======================================================================================================
"""