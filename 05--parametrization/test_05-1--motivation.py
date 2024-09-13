from cards import Card


# Motivation to use the parametrization:
# test the "finish" method without parametrize.


def test_finish_from_in_prog(cards_db):
    index = cards_db.add_card(Card("second edition", state="in prog"))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


def test_finish_from_done(cards_db):
    index = cards_db.add_card(Card("write a book", state="done"))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


def test_finish_from_todo(cards_db):
    index = cards_db.add_card(Card("create a course", state="todo"))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


# Problem:
# - redundant code
"""
$ pytest -k test_05-1 -v
***
05--parametrization/test_05-1--motivation.py::test_finish_from_in_prog PASSED
05--parametrization/test_05-1--motivation.py::test_finish_from_done PASSED
05--parametrization/test_05-1--motivation.py::test_finish_from_todo PASSED
***
"""


# not good solution
def test_finish(cards_db):
    for c in [
        Card("write a book", state="done"),
        Card("second edition", state="in prog"),
        Card("create a course", state="todo"),
    ]:
        index = cards_db.add_card(c)
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == "done"


"""
$ pytest -k test_05-1 -v
***
05--parametrization/test_05-1--motivation.py::test_finish PASSED
***
"""
# Problems:
# - one report for three tests
# - if one of the test cases fails, we don't know which one
# - pytest stops running a test when an assert fails
