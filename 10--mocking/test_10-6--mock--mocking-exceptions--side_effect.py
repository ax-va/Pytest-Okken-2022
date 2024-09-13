"""
Source code to test from "cards_proj/src/cards/cli.py":
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
def delete(card_id: int):
    with cards_db() as db:
        try:
            db.delete_card(card_id)
        except cards.InvalidCardId:
            print(f"Error: Invalid card id {card_id}")
```
"""
from helpers import cards_cli
import cards


def test_delete_invalid(mock_cards_db):
    # Mock that delete_card generates an exception by assigning
    # the exception to the mock object `side_effect` attribute.
    mock_cards_db.delete_card.side_effect = cards.api.InvalidCardId
    out = cards_cli("delete 2")
    assert "Error: Invalid card id 2" in out


"""
$ pytest -v -s 10--mocking/test_10-6--mock--mocking-exceptions--side_effect.py::test_delete_invalid
***
10--mocking/test_10-6--mock--mocking-exceptions--side_effect.py::test_delete_invalid PASSED
***
"""