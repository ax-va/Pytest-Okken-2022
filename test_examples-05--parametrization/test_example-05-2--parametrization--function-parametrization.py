"""
This is appropriate for the case "SAME TEST, DIFFERENT DATA".

pytest calls a test function, once each for every set of argument values.

Notice:
add more parameters than necessary => more clarity from the output about the differences in the test cases
"""
import pytest
from cards import Card


@pytest.mark.parametrize(
    "start_summary, start_state",
    [
        ("write a book", "done"),
        ("second edition", "in prog"),
        ("create a course", "todo"),
    ],
)
def test_finish(cards_db, start_summary, start_state):
    initial_card = Card(summary=start_summary, state=start_state)
    index = cards_db.add_card(initial_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


"""
$ pytest -k test_example-05-2 -v
...
test_examples-05--parametrization/test_example-05-2--parametrization--function-parametrization.py::test_finish[write a book-done] PASSED 
test_examples-05--parametrization/test_example-05-2--parametrization--function-parametrization.py::test_finish[second edition-in prog] PASSED
test_examples-05--parametrization/test_example-05-2--parametrization--function-parametrization.py::test_finish[create a course-todo] PASSED
...
"""


# Reduce the complexity of the test
@pytest.mark.parametrize("start_state", ["done", "in prog", "todo"])
def test_finish_simple(cards_db, start_state):
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


"""
$ pytest -k test_example-05-2 -v
...
test_examples-05--parametrization/test_example-05-2--parametrization--function-parametrization.py::test_finish_simple[done] PASSED
test_examples-05--parametrization/test_example-05-2--parametrization--function-parametrization.py::test_finish_simple[in prog] PASSED
test_examples-05--parametrization/test_example-05-2--parametrization--function-parametrization.py::test_finish_simple[todo] PASSED
...
"""