"""
Assertion Helper Function
"""
import pytest
from cards import Card


def assert_identical(c1: Card, c2: Card):
    """ Helper function """
    __tracebackhide__ = True  # Failing tests will not include this function in the traceback
    assert c1 == c2
    if c1.id != c2.id:
        pytest.fail(f"id's don't match. {c1.id} != {c2.id}")
    # equivalent:
    # assert c1.id == c2.id, f"id's don't match. {c1.id} != {c2.id}"


def test_identical():
    c1 = Card("foo", id=123)
    c2 = Card("foo", id=123)
    assert_identical(c1, c2)


def test_identical_fail():
    c1 = Card("foo", id=123)
    c2 = Card("foo", id=456)
    assert_identical(c1, c2)


"""
$ pytest 02--tests/test_02-4--helper.py
===================================================================================================== test session starts ======================================================================================================
###
collected 2 items                                                                                                                                                                                                              

02--tests/test_02-4--helper.py .F                                                                                                                                                                                         [100%]

=========================================================================================================== FAILURES ===========================================================================================================
_____________________________________________________________________________________________________ test_identical_fail ______________________________________________________________________________________________________

    def test_identical_fail():
        c1 = Card("foo", id=123)
        c2 = Card("foo", id=456)
>       assert_identical(c1, c2)
E       Failed: ids don't match. 123 != 456

02--tests/test_02-4--helper.py:24: Failed
=================================================================================================== short test summary info ====================================================================================================
FAILED 02--tests/test_02-4--helper.py::test_identical_fail - Failed: ids don't match. 123 != 456
================================================================================================= 1 failed, 1 passed in 0.06s ==================================================================================================
"""