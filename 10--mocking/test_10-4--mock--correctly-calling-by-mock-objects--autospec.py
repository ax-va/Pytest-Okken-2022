"""
Any method with any parameters can be called by a mock object.
->
- *Mock drift* = the interface being mocked changes, while the mock in the test code doesn't.
- misspelling, etc.
->
Use autospeccing by "autospec=True".

Notice:
The only exception when autospecting is not possible is if the objects are dynamic in nature.

See also:
- Python: Autospeccing
https://docs.python.org/3/library/unittest.mock.html#autospeccing
"""
from unittest import mock
import cards


def test_bad_mock():
    with mock.patch.object(cards, "CardsDB") as CardsDB:
        db = CardsDB("/some/path")
        db.path()  # good
        db.path(35)  # invalid arguments
        db.not_valid()  # invalid function


"""
$ pytest -v -s 10--mocking/test_10-4--mock--correctly-calling-by-mock-objects--autospec.py::test_bad_mock
###
10--mocking/test_10-4--mock--correctly-calling-by-mock-objects--autospec.py::test_bad_mock PASSED
###
"""


def test_good_mock():
    with mock.patch.object(cards, "CardsDB", autospec=True) as CardsDB:
        db = CardsDB("/some/path")
        db.path()  # good
        db.path(35)  # invalid arguments
        db.not_valid()  # invalid function


"""
$ pytest -v -s 10--mocking/test_10-4--mock--correctly-calling-by-mock-objects--autospec.py::test_good_mock
###
FAILED 10--mocking/test_10-4--mock--correctly-calling-by-mock-objects--autospec.py::test_good_mock - TypeError: too many positional arguments
###
"""


def test_good_mock_v2():
    with mock.patch.object(cards, "CardsDB", autospec=True) as CardsDB:
        db = CardsDB("/some/path")
        db.path()  # good
        db.not_valid()  # invalid function


"""
$ pytest -v -s 10--mocking/test_10-4--mock--correctly-calling-by-mock-objects--autospec.py::test_good_mock_v2
###
FAILED 10--mocking/test_10-4--mock--correctly-calling-by-mock-objects--autospec.py::test_good_mock_v2 - AttributeError: Mock object has no attribute 'not_valid'
###
"""