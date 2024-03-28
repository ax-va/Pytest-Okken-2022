"""
This is appropriate for the case "SAME TEST, DIFFERENT START STATE".

pytest calls the fixture with parameters, once each for every set of parameter values.
Then every test function with the fixture is called, once each for every fixture value.

Within the fixture we could have code that depends on the parameter value.
That is useful if you have set up or teardown code that needs to run for each test case.
Also, the same fixture with parameters can be used in many different test functions.
"""
import pytest
from cards import Card


@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
    return request.param


def test_finish(cards_db, start_state):
    # pytest calls start_state() three times, once each for all values in params
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


"""
$ pytest -k test_example-05-3 -v
...
test_examples-05--parametrization/test_example-05-3--parametrization--fixture-parametrization.py::test_finish[done] PASSED
test_examples-05--parametrization/test_example-05-3--parametrization--fixture-parametrization.py::test_finish[in prog] PASSED
test_examples-05--parametrization/test_example-05-3--parametrization--fixture-parametrization.py::test_finish[todo] PASSED
...
"""