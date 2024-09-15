"""
Test CLI with Typer.

Source code to test from "cards_proj/src/cards/cli.py"::
```python
import cards
import typer

app = typer.Typer(add_completion=False)


@app.command()
def version():
    print(cards.__version__)
```

Notice:
`cli_runner = CliRunner()` was moved to `helpers.py`.
"""
from cards.cli import app
from helpers import cards_cli, cli_runner


def test_typer_cli_runner():
    # to run `$ cards version`
    result = cli_runner.invoke(app, ["version"])
    print(f"\nversion: {result.stdout}")
    # to run `$ cards list -o brian`
    result = cli_runner.invoke(app, ["list", "-o", "NoName"])
    print(f"list:\n{result.stdout}")


"""
$ pytest -v -s 10--mocking/test_10-1--typer--testing-cli-with-typer--CliRunner.py::test_typer_cli_runner
***
version: 1.0.0

list:
                                        
  ID   state     owner    summary       
 ────────────────────────────────────── 
  2    in prog   NoName   do something  
***
PASSED
***
"""


# Use the `cards_cli` helper function
def test_cards_cli():
    result = cards_cli("version")
    print(f"\nversion: {result}")
    result = cards_cli("list -o NoName")
    print(f"list:\n{result}")


"""
$ pytest -v -s 10--mocking/test_10-1--typer--testing-cli-with-typer--CliRunner.py::test_cards_cli
***
version: 1.0.0
list:
                                        
  ID   state     owner    summary       
 ────────────────────────────────────── 
  2    in prog   NoName   do something
PASSED
***
"""