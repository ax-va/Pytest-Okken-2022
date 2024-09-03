"""
Mock attributes.

*Mock* = replacing a part of a system with mock objects.
Mock objects are typically intended to be objects that are used in place of the real implementation.
Mocking attributes = replacing attributes with non-original values.
Next, we mock the `__version__` attribute of `cards`.
"""
from unittest import mock
from cards.cli import app
from helpers import cli_runner
import cards


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