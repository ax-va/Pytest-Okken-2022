import pytest
import cards


def test_no_path_raises():
    with pytest.raises(TypeError):
        # In the block of code should raise a TypeError exception.
        # If no exception is raised, the test fails.
        # If the test raises a different exception, it fails.
        cards.CardsDB()


def test_raises_with_info():
    match_regex = "missing 1 .* positional argument"
    with pytest.raises(TypeError, match=match_regex):
        cards.CardsDB()


def test_raises_with_info_alt():
    with pytest.raises(TypeError) as exc_info:  # type: pytest.ExceptionInfo
        cards.CardsDB()
        expected = "missing 1 required positional argument"
        assert expected in str(exc_info.value)


"""
$ pytest 02--tests/test_02-5--exceptions.py
===================================================================================================== test session starts ======================================================================================================
***
collected 3 items                                                                                                                                                                                                              

02--tests/test_02-5--exceptions.py ...                                                                                                                                                                                    [100%]

====================================================================================================== 3 passed in 0.03s =======================================================================================================
"""