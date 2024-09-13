"""
Fail example with the assert statement
"""
from cards import Card


def test_equality_fail():
    c1 = Card("sit there", "brian")
    c2 = Card("do something", "okken")
    assert c1 == c2


if __name__ == "__main__":
    test_equality_fail()

"""
$ pytest 02--tests/test_02-2--card-fail.py
===================================================================================================== test session starts ======================================================================================================
***                                                                                                                                                                                                          

02--tests/test_02-2--card-fail.py F                                                                                                                                                                                       [100%]

=========================================================================================================== FAILURES ===========================================================================================================
______________________________________________________________________________________________________ test_equality_fail ______________________________________________________________________________________________________

    def test_equality_fail():
        c1 = Card("sit there", "brian")
        c2 = Card("do something", "okken")
>       assert c1 == c2
E       AssertionError: assert Card(summary=...odo', id=None) == Card(summary=...odo', id=None)
E         
E         Omitting 1 identical items, use -vv to show
E         Differing attributes:
E         ['summary', 'owner']
E         
E         Drill down into differing attribute summary:
E           summary: 'sit there' != 'do something'...
E         
E         ...Full output truncated (7 lines hidden), use '-vv' to show

02--tests/test_02-2--card-fail.py:7: AssertionError
=================================================================================================== short test summary info ====================================================================================================
FAILED 02--tests/test_02-2--card-fail.py::test_equality_fail - AssertionError: assert Card(summary=...odo', id=None) == Card(summary=...odo', id=None)
====================================================================================================== 1 failed in 0.12s =======================================================================================================
"""

# Show all mismatches
"""
$ pytest -vv 02--tests/test_02-2--card-fail.py
===================================================================================================== test session starts ======================================================================================================
***                                                                                                                                                                                                           

02--tests/test_02-2--card-fail.py::test_equality_fail FAILED                                                                                                                                                              [100%]

=========================================================================================================== FAILURES ===========================================================================================================
______________________________________________________________________________________________________ test_equality_fail ______________________________________________________________________________________________________

    def test_equality_fail():
        c1 = Card("sit there", "brian")
        c2 = Card("do something", "okken")
>       assert c1 == c2
E       AssertionError: assert Card(summary='sit there', owner='brian', state='todo', id=None) == Card(summary='do something', owner='okken', state='todo', id=None)
E         
E         Matching attributes:
E         ['state']
E         Differing attributes:
E         ['summary', 'owner']
E         
E         Drill down into differing attribute summary:
E           summary: 'sit there' != 'do something'
E           - do something
E           + sit there
E         
E         Drill down into differing attribute owner:
E           owner: 'brian' != 'okken'
E           - okken
E           + brian

02--tests/test_02-2--card-fail.py:7: AssertionError
=================================================================================================== short test summary info ====================================================================================================
FAILED 02--tests/test_02-2--card-fail.py::test_equality_fail - AssertionError: assert Card(summary='sit there', owner='brian', state='todo', id=None) == Card(summary='do something', owner='okken', state='todo', id=None)
====================================================================================================== 1 failed in 0.11s =======================================================================================================
"""

# With "if __name__ == "__main__":" we can start the test with Python
"""
$ python 02--tests/test_02-2--card-fail.py
Traceback (most recent call last):
  File ".../02--tests/test_02-2--card-fail.py", line 11, in <module>
    test_equality_fail()
  File ".../02--tests/test_02-2--card-fail.py", line 7, in test_equality_fail
    assert c1 == c2
AssertionError
"""