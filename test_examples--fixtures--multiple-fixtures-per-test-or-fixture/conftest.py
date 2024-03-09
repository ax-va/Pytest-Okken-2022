from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
import cards


@pytest.fixture(scope="session")
def db():
    """ CardsDB object connected to a temporary database """
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db_ = cards.CardsDB(db_path)
        yield db_
        db_.close()


@pytest.fixture(scope="function")
def empty_db(db):
    """ CardsDB object that's empty """
    db.delete_all()
    return db


@pytest.fixture(scope="session")
def some_cards():
    """ List of different Card objects """
    return [
        cards.Card("write book", "Brian", "done"),
        cards.Card("edit book", "Katie", "done"),
        cards.Card("write 2nd edition", "Brian", "todo"),
        cards.Card("edit 2nd edition", "Katie", "todo"),
    ]


@pytest.fixture(scope="function")
def non_empty_db(empty_db, some_cards):
    """ CardsDB object that's been populated with 'some_cards' """
    for c in some_cards:
        empty_db.add_card(c)
    return empty_db

# The fixture "non_empty_db" has to be of the function scope
# because it uses "empty_db", which is of the function scope.
