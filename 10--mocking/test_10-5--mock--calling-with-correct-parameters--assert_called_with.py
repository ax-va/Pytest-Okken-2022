"""
Make sure methods are called correctly.
->
Use assert_called_with.

Source code to test from "cards_proj/src/cards/api.py"::
```python
class CardsDB:
    ...
    def add_card(self, card: Card) -> int:
        ...
```

See also:
- Python: variants of `assert_called`
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called
"""
from helpers import cards_cli
import cards


def test_add_with_owner(mock_cards_db):
    # to run `$ add some task -o brian`
    cards_cli("add some task -o brian")
    expected = cards.Card("some task", owner="brian", state="todo")
    mock_cards_db.add_card.assert_called_with(expected)


"""
$ pytest -v -s 10--mocking/test_10-5--mock--calling-with-correct-parameters--assert_called_with.py::test_add_with_owner
***
10--mocking/test_10-5--mock--calling-with-correct-parameters--assert_called_with.py::test_add_with_owner PASSED
***
"""


def test_add_with_owner_failing(mock_cards_db):
    # to run `$ add some task -o brian`
    cards_cli("add some task -o brian")
    expected = cards.Card("some task", owner="Brian", state="todo")
    mock_cards_db.add_card.assert_called_with(expected)


"""
$ pytest -v -s 10--mocking/test_10-5--mock--calling-with-correct-parameters--assert_called_with.py::test_add_with_owner_failing
***
E           AssertionError: expected call not found.
E           Expected: add_card(Card(summary='some task', owner='Brian', state='todo', id=None))
E             Actual: add_card(Card(summary='some task', owner='brian', state='todo', id=None))
***
FAILED 10--mocking/test_10-5--mock--calling-with-correct-parameters--assert_called_with.py::test_add_with_owner_failing - AssertionError: expected call not found.
***
"""