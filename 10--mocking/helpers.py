from typer.testing import CliRunner
from cards.cli import app
import shlex

cli_runner = CliRunner()


def cards_cli(command_string):
    """ Helper function """
    command_list = shlex.split(command_string)
    result = cli_runner.invoke(app, command_list)
    output = result.stdout.rstrip()
    return output
