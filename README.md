## Original source code
The link to the original source code is given on the official book's side

https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/

Original installable plugin

https://github.com/okken/pytest-skip-slow

## Upgrade pip

```unix
$ python3 -m pip install -U pip
```

## Install using `pip`

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

Install from the current directory
```unix
(venv_editable) $ pip install -e .
```

Install from a directory with optional dependencies for testing
```unix
(venv_editable) $ pip install -e "./cards_proj_failed/[test]"
```

`[test]` in the `-e` parameters refers to optional dependencies for testing given in `pyproject.toml`.

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

## Python's `subprocess.run` 
https://docs.python.org/3/library/subprocess.html#subprocess.run

## Dictionary view objects
https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects