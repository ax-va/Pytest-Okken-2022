import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
import cards


@pytest.fixture()
def cards_db():
    # The default scope for fixtures is function scope
    with TemporaryDirectory() as db_dir:
        # SETUP
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        # Pass control to tests
        yield db  # Tests get to run with the CardsDB object
        # TEARDOWN
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
$ pytest 03--fixtures/a/test_03-2--setup--teardown.py
*** test session starts ***
***                                                                                                                                                                             

03--fixtures/a/test_03-2--setup--teardown.py ..                                                                   [100%]
***
"""

# Show the order of operations of tests and fixtures, including the setup and teardown phases of the fixtures
"""
$ pytest --setup-show  03--fixtures/a/test_03-2--setup--teardown.py
*** test session starts ***
***                                                                                                                                                                            

03--fixtures/a/test_03-2--setup--teardown.py 
        SETUP    F cards_db
        03--fixtures/a/test_03-2--setup--teardown.py::test_empty (fixtures used: cards_db).
        TEARDOWN F cards_db
        SETUP    F cards_db
        03--fixtures/a/test_03-2--setup--teardown.py::test_two (fixtures used: cards_db).
        TEARDOWN F cards_db
***
"""
# F in front of the fixture name indicates that the fixture is using function scope
