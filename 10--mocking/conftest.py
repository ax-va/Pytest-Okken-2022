from unittest import mock

import cards
import pytest


# Create fixture with mock object
@pytest.fixture()
def mock_cards_db():
    with mock.patch.object(
            cards, "CardsDB",
            # without "autospec=True", any method with any parameters can be called with a mock object -> mock drift
            autospec=True,
    ) as CardsDB:
        cards_db = CardsDB.return_value
        cards_db.path.return_value = "/foo/"
        yield cards_db