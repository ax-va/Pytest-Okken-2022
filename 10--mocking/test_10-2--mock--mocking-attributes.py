"""
Mock = replacing a part of a system with something else, namely mock objects.
Mocking attributes = replacing attributes with non-original values.
Next, we mock the `__version__` attribute of `cards`.
"""
from unittest import mock
from typer.testing import CliRunner
from cards.cli import app

import cards

cli_runner = CliRunner()


def test_mock_version():
    # The `__version__` attribute of cards is replaced with "1.2.3" in the `with` block
    with mock.patch.object(cards, "__version__", "1.2.3"):
        result = cli_runner.invoke(app, ["version"])
        assert result.stdout.rstrip() == "1.2.3"


"""
$ pytest -v -s 10--mocking/test_10-2--mock--mocking-attributes.py
###
10--mocking/test_10-2--mock--mocking-attributes.py::test_mock_version PASSED
###
"""