from unittest import mock
from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
import cards


# Create fixture with mock object
@pytest.fixture()
def mock_cards_db():
    """ Mock object as fixture """
    with mock.patch.object(
            cards, "CardsDB",
            # without "autospec=True", any method with any parameters can be called with a mock object -> mock drift
            autospec=True,
    ) as CardsDB:
        db = CardsDB.return_value
        db.path.return_value = "/foo/"
        yield db


# Create fixture with temporary database
@pytest.fixture(scope="session")
def cards_db():
    """ CardsDB object connected to a temporary database """
    with TemporaryDirectory() as db_dir:
        print("db_dir:", db_dir)
        print("Here")
        # SETUP
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        # Pass to tests
        yield db
        # TEARDOWN
        db.close()
    # Clean up the temporary directory
