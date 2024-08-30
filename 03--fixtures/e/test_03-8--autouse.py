import pytest
import time

# Add test times after each test, and the date and current time at the end of the session


@pytest.fixture(autouse=True, scope="session")
def footer_session_scope():
    """ Report the time at the end of a session """
    yield
    now = time.time()
    print("\n--")
    print(f"finished : {time.strftime('%d %b %X', time.localtime(now))}")
    print("-----------------")


@pytest.fixture(autouse=True)  # default: scope="function"
def footer_function_scope():
    """ Report test durations after each function """
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print(f"\ntest duration : {delta:0.3} seconds")


def test_1():
    """ Simulate long-running test """
    time.sleep(1)


def test_2():
    """ Simulate slightly longer test """
    time.sleep(1.23)


"""
$ pytest -v -s -k test_03-7
===================================================================================================== test session starts ======================================================================================================
###                                                                                                                                                                            

03--fixtures/e/test_03-8--autouse.py::test_1 PASSED
test duration : 1.0 seconds

03--fixtures/e/test_03-8--autouse.py::test_2 PASSED
test duration : 1.23 seconds

--
finished : 09 Mar 17:03:38
-----------------


=============================================================================================== 4 passed, 32 deselected in 2.28s ===============================================================================================
"""