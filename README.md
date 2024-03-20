## Original source code
https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/

## Install using PyPI

Create a virtual environment and install `pytest` on POSIX systems:
```unix
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install pytest
```
```unix
$ python3 -m pip install virtualenv
$ python3 -m virtualenv venv
$ source venv/bin/activate
(venv) $ pip install pytest
```
on Windows systems
```windows
C:\> python -m venv venv
C:\> venv\Scripts\activate.bat
(venv) C:\> pip install pytest
```
for PowerShell
```windows
C:>venv\Scripts\Activate.ps1
```

Deactivate the venv
```unix
(venv) $ deactivate
```

## Run pytest

Run `pytest` in the terminal:
```unix
$ pytest test_example-01-1--passing.py
===================================================================================================== test session starts ======================================================================================================
 ...
collected 1 item

test_example-01-1--passing.py .                                                                                                                                                                                                      [100%]

====================================================================================================== 1 passed in 0.00s =======================================================================================================
```
```unix
$ pytest -v test_example-01-1--passing.py
===================================================================================================== test session starts ======================================================================================================
...
collected 1 item

test_example-01-1--passing.py::test_passing PASSED                                                                                                                                                                                   [100%]

====================================================================================================== 1 passed in 0.00s =======================================================================================================
```

Run all tests starting with `test_` or ending with `_test` in the current working directory without traceback
```unix
$ pytest --tb=no
```

Run tests given by their names or (sub)directories in which they are located
```unix
$ pytest --tb=no test_example-01-1--passing.py test_example-01-2--failing.py
$ cd ..
$ pytest --tb=no test_examples-01
```

Run only specified functions
```unix
$ cd test_examples-01
$ pytest -v test_example-01-1--passing.py::test_passing
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
