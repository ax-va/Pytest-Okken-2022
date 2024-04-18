"""
Alternative fail example with pytest.fail() (that is not recommended)
"""
import pytest
from cards import Card


def test_with_fail():
    c1 = Card("sit there", "brian")
    c2 = Card("do something", "okken")
    if c1 != c2:
        pytest.fail("they don't match")


"""
$ pytest test_examples-02/test_example-02-3--card-alt-fail.py
===================================================================================================== test session starts ======================================================================================================
###                                                                                                                                                                                                            

test_examples-02/test_example-02-3--card-alt-fail.py F                                                                                                                                                                         [100%]

=========================================================================================================== FAILURES ===========================================================================================================
________________________________________________________________________________________________________ test_with_fail ________________________________________________________________________________________________________

    def test_with_fail():
        c1 = Card("sit there", "brian")
        c2 = Card("do something", "okken")
        if c1 != c2:
>           pytest.fail("they don't match")
E           Failed: they don't match

test_examples-02/test_example-02-3--card-alt-fail.py:12: Failed
=================================================================================================== short test summary info ====================================================================================================
FAILED test_examples-02/test_example-02-3--card-alt-fail.py::test_with_fail - Failed: they don't match
====================================================================================================== 1 failed in 0.11s =======================================================================================================
"""

