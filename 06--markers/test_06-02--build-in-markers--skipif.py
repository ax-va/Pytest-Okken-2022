import pytest
import cards
from packaging.version import parse  # third-party package
from cards import Card


@pytest.mark.skipif(
    parse(cards.__version__).major < 2,
    reason="Card < comparison not supported in 1.x",
)
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2


def test_equality():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2


"""
$ cd 06*
$ pytest test_06-02--build-in-markers--skipif.py -v -ra
***
test_06-02--build-in-markers--skipif.py::test_less_than SKIPPED (Card < comparison not supported in 1.x)
test_06-02--build-in-markers--skipif.py::test_equality PASSED

*** short test summary info ***
SKIPPED [1] test_06-02--build-in-markers--skipif.py:7: Card < comparison not supported in 1.x
***
$ cd ..
"""