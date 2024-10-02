import pytest
from cards import Card

summaries = ["short", "a bit longer"]
owners = ["First", "First M. Last"]
states = ["todo", "in prog", "done"]


# Test against a small number of combinations
@pytest.mark.parametrize(
	"summary, owner, state",
	[
		("short", "First", "todo"),
		("short", "First", "in prog"),
	],
)
def test_add_lots(cards_db, summary, owner, state):
	""" Make sure adding to db doesn't change values. """
	i = cards_db.add_card(Card(summary, owner=owner, state=state))
	card = cards_db.get_card(i)
	expected = Card(summary, owner=owner, state=state)
	assert card == expected


"""
$ cd 16*
$ pytest -v -k "16-3 and test_add_lots"
***
test_16-3--multiple-parameters.py::test_add_lots[short-First-todo] PASSED                                         [ 50%]
test_16-3--multiple-parameters.py::test_add_lots[short-First-in prog] PASSED                                      [100%]
***
$ cd ..
"""

# Test against all combinations of `summary`, `owner`, `state`.
# Stacking parametrize decorators results in the test matrix.
@pytest.mark.parametrize("state", states)
@pytest.mark.parametrize("owner", owners)
@pytest.mark.parametrize("summary", summaries)
def test_stacking(cards_db, summary, owner, state):
	""" Make sure adding to db doesn't change values. """
	i = cards_db.add_card(Card(summary, owner=owner, state=state))
	card = cards_db.get_card(i)
	expected = Card(summary, owner=owner, state=state)
	assert card == expected

# 3 * 2 * 3  = 12 test cases
"""
$ cd 16*
$ pytest -v -k "16-3 and test_stacking"
***
test_16-3--multiple-parameters.py::test_stacking[short-First-todo] PASSED                                         [  8%]
test_16-3--multiple-parameters.py::test_stacking[short-First-in prog] PASSED                                      [ 16%]
test_16-3--multiple-parameters.py::test_stacking[short-First-done] PASSED                                         [ 25%]
test_16-3--multiple-parameters.py::test_stacking[short-First M. Last-todo] PASSED                                 [ 33%]
test_16-3--multiple-parameters.py::test_stacking[short-First M. Last-in prog] PASSED                              [ 41%]
test_16-3--multiple-parameters.py::test_stacking[short-First M. Last-done] PASSED                                 [ 50%]
test_16-3--multiple-parameters.py::test_stacking[a bit longer-First-todo] PASSED                                  [ 58%]
test_16-3--multiple-parameters.py::test_stacking[a bit longer-First-in prog] PASSED                               [ 66%]
test_16-3--multiple-parameters.py::test_stacking[a bit longer-First-done] PASSED                                  [ 75%]
test_16-3--multiple-parameters.py::test_stacking[a bit longer-First M. Last-todo] PASSED                          [ 83%]
test_16-3--multiple-parameters.py::test_stacking[a bit longer-First M. Last-in prog] PASSED                       [ 91%]
test_16-3--multiple-parameters.py::test_stacking[a bit longer-First M. Last-done] PASSED                          [100%]
***
$ cd ..
"""