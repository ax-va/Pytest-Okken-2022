from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
import cards


@pytest.fixture(scope="session")
def cards_db():
    """ CardsDB object connected to a temporary database """
    with TemporaryDirectory() as db_dir:
        # SETUP
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        # Pass to tests
        yield db
        # TEARDOWN
        db.close()
    # Clean up the temporary directory


@pytest.fixture(scope="function")
def cards_db_empty(cards_db):
    """ CardsDB object that's empty """
    cards_db.delete_all()
    return cards_db


@pytest.fixture(scope="session")
def some_cards():
    """ List of different Card objects """
    return [
        cards.Card("write book", "Brian", "done"),
        cards.Card("edit book", "Katie", "done"),
        cards.Card("write 2nd edition", "Brian", "todo"),
        cards.Card("edit 2nd edition", "Katie", "todo"),
    ]


# The fixture "cards_db_non_empty" has to be of the function scope
# because it uses "cards_db_empty", which is of the function scope.
@pytest.fixture(scope="function")
def cards_db_non_empty(cards_db_empty, some_cards):
    """ CardsDB object that's been populated with 'some_cards' """
    for c in some_cards:
        cards_db_empty.add_card(c)
    return cards_db_empty
