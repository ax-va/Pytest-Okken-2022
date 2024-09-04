import hello
from typer.testing import CliRunner

cli_runner = CliRunner()


def test_full_output():
    assert hello.full_output("Foo") == "Hello, Foo!"


def test_hello_app_no_name():
    result = cli_runner.invoke(hello.app)
    assert result.stdout == "Hello, World!\n"


def test_hello_app_with_name():
    result = cli_runner.invoke(hello.app, ["Alex"])
    assert result.stdout == "Hello, Alex!\n"


# Test
"""
$ cd 12--testing-scripts-and-applications
$ cd 12-4--testing-requirements-txt-based-applications
$ pytest -v tests/test_hello.py
###
tests/test_hello.py::test_full_output PASSED                                                                      [ 33%]
tests/test_hello.py::test_hello_app_no_name PASSED                                                                [ 66%]
tests/test_hello.py::test_hello_app_with_name PASSED                                                              [100%]
###
"""

# Test by using tox with installing side packages given in `requirements.txt`
"""
$ cd 12--testing-scripts-and-applications
$ cd 12-4--testing-requirements-txt-based-applications
$ tox
###
  py310: OK (3.61=setup[3.37]+cmd[0.24] seconds)
  py311: OK (2.78=setup[2.55]+cmd[0.24] seconds)
  congratulations :) (6.44 seconds)
###
"""