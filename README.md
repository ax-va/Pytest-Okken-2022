## Original source code
The link to the original source code is given on the official book's side

https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/

## Install using PyPI

Create a virtual environment, activate it on POSIX systems, and install `pytest`
```unix
$ python3 -m venv my_venv
$ source my_venv/bin/activate
(my_venv) $ pip install pytest
```
or using `virtualenv`
```unix
$ python3 -m pip install virtualenv
$ python3 -m virtualenv my_venv
$ source my_venv/bin/activate
(my_venv) $ pip install pytest
```
Deactivate the venv
```unix
(my_venv) $ deactivate
```
Create a virtual environment, activate it on Windows systems, and install `pytest`
```windows
C:\> python -m venv my_venv
C:\> my_venv\Scripts\activate.bat
(my_venv) C:\> pip install pytest
```
Activate in PowerShell
```windows
C:>my_venv\Scripts\Activate.ps1
```

## Run pytest

Run a test modul:
```unix
$ pytest 01-introduction/test_01-1--passing.py
```

Run a test modul with the `--verbose` or `-v` flag:
```unix
$ pytest -v 01-introduction/test_01-1--passing.py
```

Run all tests starting with `test_` or ending with `_test` in the current working directory without traceback
```unix
$ pytest --tb=no
```

Run tests given by their names or (sub)directories in which they are located
```unix
$ pytest --tb=no 01-introduction/test_01-1--passing.py 01-introduction/test_01-2--failing.py
$ pytest --tb=no 01-introduction
```

Run only specified functions
```unix
$ pytest -v 01-introduction/test_01-1--passing.py::test_passing
```

## Conventions to keep your test code discoverable by `pytest`

- `test_<something>.py` or `<something>_test.py` for files
- `test_<something>` for methods and functions
- `Test<Something>` for classes

## Original source code: 

https://pragprog.com/titles/bopytest2/source_code

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