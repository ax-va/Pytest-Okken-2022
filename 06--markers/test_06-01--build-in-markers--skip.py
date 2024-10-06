import pytest
from cards import Card


@pytest.mark.skip(reason="Card doesn't support < comparison yet")
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    # Exception "TypeError: '<' not supported between instances of 'Card' and 'Card'"  would be thrown.
    # The test would be failed, but that can be supported in a future version.
    assert c1 < c2


def test_equality():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2


"""
$ cd 06*
$ pytest test_06-01--build-in-markers--skip.py --tb=short
***
test_06-01--build-in-markers--skip.py s.
***
$ cd ..
"""

# Display a reason
"""
$ cd 06*
$ test_06-01--build-in-markers--skip.py -v -ra
***
test_06-01--build-in-markers--skip.py::test_less_than SKIPPED (Card doesn't support < comparison yet)
test_06-01--build-in-markers--skip.py::test_equality PASSED

*** short test summary info ***
SKIPPED [1] test_06-01--build-in-markers--skip.py:5: Card doesn't support < comparison yet
***
$ cd ..
"""