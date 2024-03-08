"""
Quick tests to understand how the data structure works
"""
from cards import Card


def test_field_access():
    c = Card("something", "brian", "todo", 123)
    assert c.summary == "something"
    assert c.owner == "brian"
    assert c.state == "todo"
    assert c.id == 123


def test_defaults():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None


def test_equality():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("something", "brian", "todo", 123)
    assert c1 == c2


def test_equality_with_diff_ids():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("something", "brian", "todo", 4567)
    assert c1 == c2


def test_inequality():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("completely different", "okken", "done", 123)
    assert c1 != c2


def test_from_dict():
    c1 = Card("something", "brian", "todo", 123)
    c2_dict = {
        "summary": "something",
        "owner": "brian",
        "state": "todo",
        "id": 123,
    }
    c2 = Card.from_dict(c2_dict)
    assert c1 == c2


def test_to_dict():
    c1 = Card("something", "brian", "todo", 123)
    c2 = c1.to_dict()
    c2_expected = {
        "summary": "something",
        "owner": "brian",
        "state": "todo",
        "id": 123,
    }
    assert c2 == c2_expected


"""
$ pytest test_examples/test_example-2-1--card.py
===================================================================================================== test session starts ======================================================================================================
platform linux -- Python 3.11.0rc1, pytest-8.0.1, pluggy-1.4.0
rootdir: /home/delorian/PycharmProjects/pytest-Okken-2022
collected 7 items                                                                                                                                                                                                              

test_examples/test_example-2-1--card.py .......                                                                                                                                                                            [100%]

====================================================================================================== 7 passed in 0.06s =======================================================================================================

$ pytest test_examples/test_example-2-1--card.py --verbose
===================================================================================================== test session starts ======================================================================================================
...
collected 7 items                                                                                                                                                                                                              

test_examples/test_example-2-1--card.py::test_field_access PASSED                                                                                                                                                          [ 14%]
test_examples/test_example-2-1--card.py::test_defaults PASSED                                                                                                                                                              [ 28%]
test_examples/test_example-2-1--card.py::test_equality PASSED                                                                                                                                                              [ 42%]
test_examples/test_example-2-1--card.py::test_equality_with_diff_ids PASSED                                                                                                                                                [ 57%]
test_examples/test_example-2-1--card.py::test_inequality PASSED                                                                                                                                                            [ 71%]
test_examples/test_example-2-1--card.py::test_from_dict PASSED                                                                                                                                                             [ 85%]
test_examples/test_example-2-1--card.py::test_to_dict PASSED                                                                                                                                                               [100%]

====================================================================================================== 7 passed in 0.05s =======================================================================================================
"""