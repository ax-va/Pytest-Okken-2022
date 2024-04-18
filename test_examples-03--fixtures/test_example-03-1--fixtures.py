"""
Test fixtures allow the separation of "getting ready for" and "cleaning up after" code from test functions.
Exceptions during the test code in test functions are reported as "Fail",
while ones during fixtures in test functions as result in "Error".
"""
import pytest


@pytest.fixture()
def some_data():
    """ Return answer to ultimate question """
    return 42


def test_some_data(some_data):
    """ Use fixture return value in a test """
    assert some_data == 42


"""
$ pytest -k test_example-03-1
===================================================================================================== test session starts ======================================================================================================
###                                                                                                                                                                              

test_examples-03--fixtures/test_example-03-1--fixtures.py .                                                                                                                                                                            [100%]

=============================================================================================== 1 passed, 20 deselected in 0.04s ===============================================================================================
"""
