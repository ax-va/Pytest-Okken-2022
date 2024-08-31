"""
Separating a test into stages:
"getting ready to do something", "doing something", and "checking to see if it worked".
That is known as the "Arrange-Act-Assert" or "Given-When-Then" pattern.
A common anti-pattern is an "Arrange-Assert-Act-Assert-Act-Assert..." pattern.
"""
from cards import Card


def test_to_dict():
    # ARRANGE / GIVEN a Card object with known contents
    c1 = Card("something", "brian", "todo", 123)
    # ACT / WHEN we call to_dict() on the object
    c2 = c1.to_dict()
    # ASSERT / THEN the result will be a dictionary with known content
    c2_expected = {
        "summary": "something",
        "owner": "brian",
        "state": "todo",
        "id": 123,
    }
    assert c2 == c2_expected
