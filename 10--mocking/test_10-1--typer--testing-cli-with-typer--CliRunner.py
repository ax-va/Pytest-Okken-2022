"""
Testing CLI with Typer.

For example, the code of the CLI `version` function is
```python
import cards
import typer

app = typer.Typer(add_completion=False)


@app.command()
def version():
    print(cards.__version__)
```
"""
from typer.testing import CliRunner
from cards.cli import app

import shlex

cli_runner = CliRunner()


def test_typer_cli_runner():
    # to run `cards version`
    result = cli_runner.invoke(app, ["version"])
    print(f"\nversion: {result.stdout}")
    # to run `cards list -o brian`
    result = cli_runner.invoke(app, ["list", "-o", "NoName"])
    print(f"list:\n{result.stdout}")


"""
$ pytest -v -s 10--mocking/test_10-1--typer--testing-cli-with-typer--CliRunner.py::test_typer_cli_runner
###
version: 1.0.0

list:
                                        
  ID   state     owner    summary       
 ────────────────────────────────────── 
  2    in prog   NoName   do something  
PASSED
###
"""


def cards_cli(command_string):
    """ Helper function """
    command_list = shlex.split(command_string)
    result = cli_runner.invoke(app, command_list)
    output = result.stdout.rstrip()
    return output


def test_cards_cli():
    result = cards_cli("version")
    print(f"\nversion: {result}")
    result = cards_cli("list -o NoName")
    print(f"list:\n{result}")


"""
$ pytest -v -s 10--mocking/test_10-1--typer--testing-cli-with-typer--CliRunner.py::test_cards_cli
###
version: 1.0.0
list:
                                        
  ID   state     owner    summary       
 ────────────────────────────────────── 
  2    in prog   NoName   do something
PASSED
###
"""