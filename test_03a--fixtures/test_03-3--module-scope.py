import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
import cards


@pytest.fixture(scope="module")
def cards_db():
    # The default scope for fixtures is function scope.
    # We changed it to "module".
    with TemporaryDirectory() as db_dir:
        # SETUP
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        # Pass control to tests
        yield db
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
$ pytest --setup-show -k test_03-3
===================================================================================================== test session starts ======================================================================================================
###                                                                                                                                                                              

test_03a--fixtures/test_03-3--module-scope.py 
    SETUP    M cards_db
        test_03a--fixtures/test_03-3--module-scope.py::test_empty (fixtures used: cards_db).
        test_03a--fixtures/test_03-3--module-scope.py::test_two (fixtures used: cards_db).
    TEARDOWN M cards_db

=============================================================================================== 2 passed, 23 deselected in 0.07s ===============================================================================================
"""
# M in front of the fixture name indicates that the fixture is using module scope
