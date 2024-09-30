"""
The `ids` argument to the `@pytest.mark.parametrize` decorator can be a function or an iterable instance.
The best practice is to use `.values()` as parameters and `.keys()` as ids.
"""
import pytest
from cards import Card


card_list = [
	Card("foo", state="todo"),
	Card("foo", state="in prog"),
	Card("foo", state="done"),
]

# Identifiers can be created by `str` or `repr` methods.
# Here, the IDs are using the dataclass attributes resulting in a string like
# `Card(summary='foo', owner=None, state='done', id=None)`.
@pytest.mark.parametrize("starting_card", card_list, ids=str)
def test_finish_v3(cards_db, starting_card):
	index = cards_db.add_card(starting_card)
	cards_db.finish(index)
	card = cards_db.get_card(index)
	assert card.state == "done"


"""
$ cd 16*
$ pytest -v -k "16-2 and test_finish_v3"
***
test_16-2--custom-identifiers.py::test_finish_v3[Card(summary='foo', owner=None, state='todo', id=None)] PASSED         [ 33%]
test_16-2--custom-identifiers.py::test_finish_v3[Card(summary='foo', owner=None, state='in prog', id=None)] PASSED      [ 66%]
test_16-2--custom-identifiers.py::test_finish_v3[Card(summary='foo', owner=None, state='done', id=None)] PASSED         [100%]
***
$ cd ..
"""
# -> Hard to read identifiers.


# Set a custom ID function as a lambda function
@pytest.mark.parametrize("starting_card", card_list, ids=lambda c: c.state)
def test_finish_v4(cards_db, starting_card):
	index = cards_db.add_card(starting_card)
	cards_db.finish(index)
	card = cards_db.get_card(index)
	assert card.state == "done"
"""
$ cd 16*
$ pytest -v -k "16-2 and test_finish_v4"
***
test_16-2--custom-identifiers.py::test_finish_v4[todo] PASSED                                                     [ 33%]
test_16-2--custom-identifiers.py::test_finish_v4[in prog] PASSED                                                  [ 66%]
test_16-2--custom-identifiers.py::test_finish_v4[done] PASSED                                                     [100%]
***
$ cd ..
"""


# Use `pytest.param`
# (used earlier in "06--markers" to add markers to parametrization values)
# for special treatment.
card_list2 = [
	pytest.param(Card("foo", state="todo"), id="special"),
	Card("foo", state="in prog"),
	Card("foo", state="done"),
]

@pytest.mark.parametrize("starting_card", card_list2, ids=lambda c: c.state)
def test_finish_v5(cards_db, starting_card):
	index = cards_db.add_card(starting_card)
	cards_db.finish(index)
	card = cards_db.get_card(index)
	assert card.state == "done"


"""
$ cd 16*
$ pytest -v -k "16-2 and test_finish_v5"
***
test_16-2--custom-identifiers.py::test_finish_v5[special] PASSED                                                  [ 33%]
test_16-2--custom-identifiers.py::test_finish_v5[in prog] PASSED                                                  [ 66%]
test_16-2--custom-identifiers.py::test_finish_v5[done] PASSED                                                     [100%]
***
$ cd ..
"""

# Use the ID as a key to a dictionary
text_variants = {
	"Short": "x",
	"With Spaces": "x y z",
	"End In Spaces": "x",
	"Mixed Case": "SuMmArY wItH MiXeD cAsE",
	"Unicode": "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾",
	"Newlines": "a\nb\nc",
	"Tabs": "a\tb\tc",
}

# Use `.values()` as parameter list and `.keys()` as ids list
@pytest.mark.parametrize("variant", text_variants.values(), ids=text_variants.keys())
def test_summary_variants(cards_db, variant):
	i = cards_db.add_card(Card(summary=variant))
	c = cards_db.get_card(i)
	assert c.summary == variant


"""
$ cd 16*
$ pytest -v -k "16-2 and test_summary_variants"
***
test_16-2--custom-identifiers.py::test_summary_variants[Short] PASSED                                             [ 14%]
test_16-2--custom-identifiers.py::test_summary_variants[With Spaces] PASSED                                       [ 28%]
test_16-2--custom-identifiers.py::test_summary_variants[End In Spaces] PASSED                                     [ 42%]
test_16-2--custom-identifiers.py::test_summary_variants[Mixed Case] PASSED                                        [ 57%]
test_16-2--custom-identifiers.py::test_summary_variants[Unicode] PASSED                                           [ 71%]
test_16-2--custom-identifiers.py::test_summary_variants[Newlines] PASSED                                          [ 85%]
test_16-2--custom-identifiers.py::test_summary_variants[Tabs] PASSED                                              [100%]
***
$ cd ..
"""