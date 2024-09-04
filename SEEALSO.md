## pytest site

https://pytest.org

## Demo of Python failure reports with pytest

https://doc.pytest.org/en/latest/example/reportingdemo.html

## Assertion rewriting

https://docs.pytest.org/en/latest/how-to/assert.html#assertion-introspection-details

## ExceptionInfo

https://docs.pytest.org/en/latest/reference/reference.html#exceptioninfo

## The Arrange-Act-Assert or Given-When-Then pattern

https://xp123.com/3a-arrange-act-assert/

https://en.wikipedia.org/wiki/Test-driven_development

https://dannorth.net/introducing-bdd/

## Pathlib

https://docs.python.org/3/library/pathlib.html#basic-use

## pytest fixtures

https://docs.pytest.org/en/latest/reference/fixtures.html

## pytest pytest_generate_tests metafunc

https://docs.pytest.org/en/latest/reference/reference.html#metafunc

## Coverage.py
The preferred Python coverage tool that measures code coverage

https://coverage.readthedocs.io/en/

```unix
$ pip install coverage
```

## pytest-cov
A popular pytest plugin often used in conjunction with coverage.py

https://pytest-cov.readthedocs.io/en/latest/

```unix
$ pip install pytest-cov
```

## unittest.mock

https://docs.python.org/3/library/unittest.mock.html

## Typer

Typer is a library for building CLI applications.

https://pypi.org/project/typer

## Python: Autospeccing
https://docs.python.org/3/library/unittest.mock.html#autospeccing

## Python: variants of assert_called 
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called

## Plugins to assist mocking

- `pytest-mock` for general-purpose mocking

The `mocker` fixture cleans up after itself, so a `with` block must not be used.

https://pypi.org/project/pytest-mock/

- `pytest-postgresql`, `pytest-mongo`, `pytest-mysql`, and `pytest-dynamodb` for mocking database access

- `pytest-httpserver` for mocking HTTP servers

- `responses` and `betamax` for mocking requests

- `pytest-rabbitmq`, `pytest-solr`, `pytest-elasticsearch`, `pytest-redis`, and others