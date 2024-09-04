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
