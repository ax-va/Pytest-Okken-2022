"""
- v1:
The multiple-layer approach tests the *behavior*, making sure the outcome is as desired.

- v2:
Mocking tests the CLI *implementation*, making sure a specific API call was called with specific parameters.
"""
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from helpers import cards_cli
import pytest
import cards


def cards_db_cm(db_dir: str):
    """
    The `cards_db` context manager similar to one in `cli.py`
    with the only essential difference that `db_dir` must be set.
    """
    @contextmanager
    def cm():
        db = cards.CardsDB(Path(db_dir))
        yield db
        db.close()
    return cm


@pytest.fixture(scope="session")
def cards_db():
    """ Session fixture """
    with TemporaryDirectory() as db_dir:
        yield cards_db_cm(db_dir)


# Test CLI by using API, i.e. without mocking
def test_add_with_owner_v1(cards_db):
    # Overwrite `cards_db` defined in `cli.py` with one given by the fixture,
    # making sure we use the other database to test.
    cards.cli.cards_db = cards_db
    cards_cli("add some NEW task -o ax-va")
    expected = cards.Card("some NEW task", owner="ax-va", state="todo")
    with cards.cli.cards_db() as db:
        all_cards = db.list_cards()
        assert len(all_cards) == 1
        assert all_cards[0] == expected


"""
$ pytest -v -s 10--mocking/test_10-7--testing-at-multiple-layers-to-avoid-mocking.py::test_add_with_owner_v1
###
10--mocking/test_10-7--testing-at-multiple-layers-to-avoid-mocking.py::test_add_with_owner_v1 PASSED
###
"""


# Test CLI without using API, i.e. with mocking
def test_add_with_owner_v2(mock_cards_db):
    cards_cli("add some task -o AX-VA")
    expected = cards.Card("some task", owner="AX-VA", state="todo")
    mock_cards_db.add_card.assert_called_with(expected)


"""
$ pytest -v -s 10--mocking/test_10-7--testing-at-multiple-layers-to-avoid-mocking.py::test_add_with_owner_v2
###
10--mocking/test_10-7--testing-at-multiple-layers-to-avoid-mocking.py::test_add_with_owner_v2 PASSED
###
"""