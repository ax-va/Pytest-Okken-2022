def test_failing():
    assert (1, 2, 3) == (3, 2, 1)


# Run pytest in the terminal:
"""
$ pytest test_01-2--failing.py
===================================================================================================== test session starts ======================================================================================================
###
collected 1 item

test_01-2--failing.py F                                                                                                                                                                                                      [100%]

=========================================================================================================== FAILURES ===========================================================================================================
_________________________________________________________________________________________________________ test_failing _________________________________________________________________________________________________________

    def test_failing():
>       assert (1, 2, 3) == (3, 2, 1)
E       assert (1, 2, 3) == (3, 2, 1)
E
E         At index 0 diff: 1 != 3
E         Use -v to get more diff

test_01-2--failing.py:2: AssertionError
=================================================================================================== short test summary info ====================================================================================================
FAILED test_01-2--failing.py::test_failing - assert (1, 2, 3) == (3, 2, 1)
====================================================================================================== 1 failed in 0.01s =======================================================================================================
"""

"""
$ pytest -v test_01-2--failing.py
===================================================================================================== test session starts ======================================================================================================
###
collected 1 item

test_01-2--failing.py::test_failing FAILED                                                                                                                                                                                   [100%]

=========================================================================================================== FAILURES ===========================================================================================================
_________________________________________________________________________________________________________ test_failing _________________________________________________________________________________________________________

    def test_failing():
>       assert (1, 2, 3) == (3, 2, 1)
E       AssertionError: assert (1, 2, 3) == (3, 2, 1)
E
E         At index 0 diff: 1 != 3
E
E         Full diff:
E           (
E         +     1,
E         +     2,...
E
E         ...Full output truncated (4 lines hidden), use '-vv' to show

test_01-2--failing.py:2: AssertionError
=================================================================================================== short test summary info ====================================================================================================
FAILED test_01-2--failing.py::test_failing - AssertionError: assert (1, 2, 3) == (3, 2, 1)
====================================================================================================== 1 failed in 0.01s =======================================================================================================
"""