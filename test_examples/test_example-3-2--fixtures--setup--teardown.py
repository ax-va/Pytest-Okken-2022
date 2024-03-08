import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
import cards


@pytest.fixture()
def cards_db():
    with TemporaryDirectory() as db_dir:
        # setup:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        # Pass control to tests
        yield db  # Tests get to run with the CardsDB object
        # teardown:
        # Guaranteed to run regardless of what happens during the tests
        db.close()
    # Clean up the temporary directory


def test_empty(cards_db):
    assert cards_db.count() == 0


def test_two(cards_db):
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2


"""
$ pytest -k test_example-3-2
===================================================================================================== test session starts ======================================================================================================
...                                                                                                                                                                             

test_examples/test_example-3-2--fixtures--setup--teardown.py ..                                                                                                                                                          [100%]

=============================================================================================== 2 passed, 21 deselected in 0.04s ===============================================================================================
"""
