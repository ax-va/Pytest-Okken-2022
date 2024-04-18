"""
pytest_generate_tests is a hook function.

pytest_generate_tests is especially useful to modify the parametrization list at test collection time.

Some use cases:
- parametrization list on a command-line flag:
metafunc.config.getoption("--<some_flag>")
- parametrization list of a parameter based on the presence of another parameter, e.g.
metafunc.parametrize("planet, moon", [('Earth', 'Moon'), ('Mars', 'Deimos'), ('Mars', 'Phobos'),])
"""
from cards import Card


def pytest_generate_tests(metafunc):
    if "start_state" in metafunc.fixturenames:
        metafunc.parametrize("start_state", ["done", "in prog", "todo"])


def test_finish(cards_db, start_state):
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


"""
$ pytest -k test_example-05-4 -v
###
test_examples-05--parametrization/test_example-05-4--parametrization--pytest_generate_tests.py::test_finish[done] PASSED
test_examples-05--parametrization/test_example-05-4--parametrization--pytest_generate_tests.py::test_finish[in prog] PASSED
test_examples-05--parametrization/test_example-05-4--parametrization--pytest_generate_tests.py::test_finish[todo] PASSED
###
"""