import pytest
from cards import Card, InvalidCardId

# Add file-level markers with pytestmark = pytest.mark.<marker_name>
pytestmark = pytest.mark.smoke1
# or many markers
# pytestmark = [pytest.mark.smoke2, pytest.mark.smoke3]


# Use class-level markers.
# Effectively marks each test method in the class with the same marker.
@pytest.mark.smoke4
class TestFinish:
    def test_finish_from_todo(self, cards_db):
        index = cards_db.add_card(Card("foo", state="todo"))
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == "done"

    def test_finish_from_in_prog(self, cards_db):
        index = cards_db.add_card(Card("foo", state="in prog"))
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == "done"

    def test_finish_from_done(self, cards_db):
        index = cards_db.add_card(Card("foo", state="done"))
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == "done"


# Mark function parametrization.
# Add the decorator before or after @pytest.mark.parametrize to mark all the parameters:
# @pytest.mark.smoke6
@pytest.mark.parametrize(
    "start_state",
    [
        "todo",
        pytest.param("in prog", marks=pytest.mark.smoke5),  # or marks=[pytest.mark.smoke1, pytest.mark.smoke2]
        "done",
    ],
)
# @pytest.mark.smoke7
def test_finish_func(cards_db, start_state):
    index = cards_db.add_card(Card("foo", state=start_state))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


# Mark fixture parametrization
@pytest.fixture(
    params=[
        "todo",
        pytest.param("in prog", marks=pytest.mark.smoke8),
        "done",
    ]
)
def start_state_fixture(request):
    return request.param


def test_finish_fix(cards_db, start_state_fixture):
    index = cards_db.add_card(Card("foo", state=start_state_fixture))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


# Add many markers
@pytest.mark.smoke
@pytest.mark.exception
def test_finish_non_existent(cards_db):
    index = 12345  # index is invalid
    with pytest.raises(InvalidCardId):
        cards_db.finish(index)


# Run all the tests in the file
"""
$ cd 06--markers
$ pytest -m smoke1 -v
***
test_06-05--custom-markers--files--classes--parameters.py::TestFinish::test_finish_from_todo PASSED
test_06-05--custom-markers--files--classes--parameters.py::TestFinish::test_finish_from_in_prog PASSED
test_06-05--custom-markers--files--classes--parameters.py::TestFinish::test_finish_from_done PASSED
test_06-05--custom-markers--files--classes--parameters.py::test_finish_func[todo] PASSED
test_06-05--custom-markers--files--classes--parameters.py::test_finish_func[in prog] PASSED
test_06-05--custom-markers--files--classes--parameters.py::test_finish_func[done] PASSED
test_06-05--custom-markers--files--classes--parameters.py::test_finish_fix[todo] PASSED
test_06-05--custom-markers--files--classes--parameters.py::test_finish_fix[in prog] PASSED
test_06-05--custom-markers--files--classes--parameters.py::test_finish_fix[done] PASSED
test_06-05--custom-markers--files--classes--parameters.py::test_finish_non_existent PASSED
***
$ cd ..
"""

# Run all the tests in TestFinish
"""
$ cd 06--markers
$ pytest -m smoke4 -v
***
test_06-05--custom-markers--files--classes--parameters.py::TestFinish::test_finish_from_todo PASSED
test_06-05--custom-markers--files--classes--parameters.py::TestFinish::test_finish_from_in_prog PASSED
test_06-05--custom-markers--files--classes--parameters.py::TestFinish::test_finish_from_done PASSED
***
$ cd ..
"""

# Run all the tests with specific function parametrization
"""
$ cd 06--markers
$ pytest -m smoke5 -v
***
test_06-05--custom-markers--files--classes--parameters.py::test_finish_func[in prog] PASSED
***
$ cd ..
"""

# Run all the tests with specific fixture parametrization
"""
$ pytest -m smoke8 -v
***
test_06-05--custom-markers--files--classes--parameters.py::test_finish_fix[in prog] PASSED
***
"""

# Run the tests with many markers
"""
$ pytest -m smoke -v
***
test_06-04--custom-markers.py::test_start PASSED
test_06-05--custom-markers--files--classes--parameters.py::test_finish_non_existent PASSED
***
"""

"""
$ pytest -m exception -v
***
test_06-04--custom-markers.py::test_start_non_existent PASSED
test_06-05--custom-markers--files--classes--parameters.py::test_finish_non_existent PASSED
***
"""