import pytest
from cards import Card


# All parameter's values are string values
@pytest.mark.parametrize("start_state", ["done", "in prog", "todo"])
def test_finish_v1(cards_db, start_state):
	c = Card("write a book", state=start_state)
	index = cards_db.add_card(c)
	cards_db.finish(index)
	card = cards_db.get_card(index)
	assert card.state == "done"


"""
$ cd 16*
$ pytest -v -k "16-1 and test_finish_v1"
***
test_16-1--complex-values.py::test_finish_v1[done] PASSED                                                         [ 33%]
test_16-1--complex-values.py::test_finish_v1[in prog] PASSED                                                      [ 66%]
test_16-1--complex-values.py::test_finish_v1[todo] PASSED                                                         [100%]
***
$ cd ..
"""


# All parameter's values are Card instances
@pytest.mark.parametrize(
	"starting_card",
	[
		Card("foo", state="todo"),
		Card("foo", state="in prog"),
		Card("foo", state="done"),
		],
	)
def test_finish_v2(cards_db, starting_card):
	index = cards_db.add_card(starting_card)
	cards_db.finish(index)
	card = cards_db.get_card(index)
	assert card.state == "done"


"""
$ cd 16*
$ pytest -v -k "16-1 and test_finish_v2"
***
test_16-1--complex-values.py::test_finish_v2[starting_card0] PASSED                                               [ 33%]
test_16-1--complex-values.py::test_finish_v2[starting_card1] PASSED                                               [ 66%]
test_16-1--complex-values.py::test_finish_v2[starting_card2] PASSED                                               [100%]
***
$ cd ..
"""
# -> Numbered identifiers `starting_card0`, `starting_card1`, `starting_card2` are not informative.