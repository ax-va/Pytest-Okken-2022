"""
Mock classes and methods.

*Mock* = replacing a part of a system with mock objects.
*Mock drift* = the interface being mocked changes, while the mock in the test code doesn't.

Next, we mock `cards.CardsDB()` and its `path()`, then `config()` as example.

Source code to test:
```python
import cards
import typer
from contextlib import contextmanager

app = typer.Typer(add_completion=False)


@contextmanager
def cards_db():
    db_path = get_path()
    db = cards.CardsDB(db_path)
    yield db
    db.close()


@app.command()
def config():
    with cards_db() as db:  # a cards.CardsDB object returned
        print(db.path())
```
"""
from unittest import mock
from cards.cli import app
from helpers import cli_runner
import cards


def test_mock_CardsDB():
    with mock.patch.object(cards, "CardsDB") as MockCardsDB:
        print("\nclass:\t\t", f"{MockCardsDB=}")
        print("class instance:\t", f"{MockCardsDB.return_value=}")
        with cards.cli.cards_db() as db:
            print("mock object:\t", f"{db=}")


"""
$ pytest -v -s 10--mocking/test_10-3--mock--typer--mocking-classes-and-methods.py::test_mock_CardsDB
###
class:           MockCardsDB=<MagicMock name='CardsDB' id='136007464120144'>
class instance:  MockCardsDB.return_value=<MagicMock name='CardsDB()' id='136007468716176'>
mock object:     db=<MagicMock name='CardsDB()' id='136007468716176'>
PASSED
###
"""


def test_mock_path():
    with mock.patch.object(cards, "CardsDB") as MockCardsDB:
        # MockCardsDB.return_value returns a class instance.
        # MockCardsDB.return_value.path returns a method.
        # MockCardsDB.return_value.path.return_value returns a return value of the method.
        # Change the *behavior* when someone calls CardsDB().path().
        MockCardsDB.return_value.path.return_value = "/foo/"
        with cards.cli.cards_db() as db:
            print(f"\n{db.path=}")
            print(f"{db.path()=}")


"""
$ pytest -v -s 10--mocking/test_10-3--mock--typer--mocking-classes-and-methods.py::test_mock_path
###
db.path=<MagicMock name='CardsDB().path' id='128360958775568'>
db.path()='/foo/'
PASSED
###
"""


# Final test with mock and Typer
def test_config(mock_cards_db):
    # to run `$ cards config`
    result = cli_runner.invoke(app, ["config"])
    assert result.stdout.rstrip() == "/foo/"


"""
$ pytest -v -s 10--mocking/test_10-3--mock--typer--mocking-classes-and-methods.py::test_config
###
10--mocking/test_10-3--mock--typer--mocking-classes-and-methods.py::test_config PASSED
###
"""