import pytest
from math import pi


@pytest.fixture(scope="session", name="pi")
def _pi():
    """ The rounded Pi """
    yield int(pi)


def test_rounded_pi(pi):
    print(f"\nThe false Pi is {pi}")
    assert pi == 3


"""
$ pytest -v -s -k test_03-9
===================================================================================================== test session starts ======================================================================================================
###                                                                                                                                                                             

test_03--fixtures/a/test_03-9--fixture-renaming.py::test_rounded_pi 
The false Pi is 3
PASSED

=============================================================================================== 1 passed, 36 deselected in 0.04s ===============================================================================================
"""
