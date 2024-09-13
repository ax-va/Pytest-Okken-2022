def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


# Run pytest in the terminal:
"""
$ pytest 01--introduction/test_01-1--passing.py
===================================================================================================== test session starts ======================================================================================================
***
collected 1 item

01--introduction/test_01-1--passing.py .                                                                                                                                                                                  [100%]

====================================================================================================== 1 passed in 0.00s =======================================================================================================
"""

"""
$ pytest -v 01--introduction/test_01-1--passing.py
===================================================================================================== test session starts ======================================================================================================
***
collected 1 item

01--introduction/test_01-1--passing.py::test_passing PASSED                                                                                                                                                                100%]

====================================================================================================== 1 passed in 0.00s =======================================================================================================
"""