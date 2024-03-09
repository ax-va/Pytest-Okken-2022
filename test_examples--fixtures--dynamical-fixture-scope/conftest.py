from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
import cards


def cards_db_scope(fixture_name, config):
    if config.getoption("--func-db", None):
        return "function"
    return "session"


@pytest.fixture(scope=cards_db_scope)
def cards_db():
    """ CardsDB object connected to a temporary database """
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


def pytest_addoption(parser):
    parser.addoption(
        "--func-db",
        action="store_true",
        default=False,
        help="new db for each test",
    )
