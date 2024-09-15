import pytest
from cards import Card, InvalidCardId


# Add a custom marker with @pytest.mark.<marker_name>
@pytest.mark.smoke
def test_start(cards_db):
    """
    Start changes state from "todo" to "in prog".
    """
    index = cards_db.add_card(Card("foo", state="todo"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"


# Add a custom marker with @pytest.mark.<marker_name>
@pytest.mark.exception
def test_start_non_existent(cards_db):
    """
    Shouldn't be able to start a non-existent card.
    """
    index = 12345  # index is invalid
    with pytest.raises(InvalidCardId):
        cards_db.start(index)


# If the "smoke" mark is not registered in pytest.ini, we receive a warning
"""
$ cd 06--markers
$ pytest -m smoke -v
***
test_06-04--custom-markers.py::test_start PASSED
***
*** warnings summary ***
06--markers/test_06-04--custom-markers.py:5
  ***/06--markers/test_06-04--custom-markers.py:5: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.smoke

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
***
$ cd ..
"""

# If the "smoke" mark is registered in pytest.ini, we don't receive a warning
"""
$ cd 06--markers
$ pytest -m smoke -v
***
test_06-04--custom-markers.py::test_start PASSED
***
$ cd ..
"""

"""
$ cd 06--markers
$ pytest -m exception -v
***
test_06-04--custom-markers.py::test_start_non_existent PASSED
***
% cd ..
"""