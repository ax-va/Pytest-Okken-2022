# Pytest-Okken-2022

These **pytest** examples are based on the book *"Python Testing with pytest: Simple, Rapid, Effective, 
and Scalable"*, Second Edition, written by Brian Okken and published by The Pragmatic Programmers in 2022.
It also covers how to use **Coverage.py** and **tox** with **pytest**.

Also see the `pytest-summary` directory for quick and easy information about **pytest** features.
The Python versions used in the examples are 3.10, 3.11, and 3.12. 
The third-party packages are listed in `requirements.txt`.

## Original source code
The link to the original source code is given on the official book's side

https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/

Original installable plugin for `15--building-plugins`

https://github.com/okken/pytest-skip-slow

## Upgrade pip

```unix
$ python3 -m pip install -U pip
```

## Install using `pip`

As of Python 3.3, the build-in `venv` package created a virtual environment
`python -m venv env_dir_name [--prompt my_proj]`.
The `--prompt` parameter is optional. If it is not supplied, the prompt will match the directory name.
As of Python 3.9, providing `--prompt .` will tell `venv` to use the parent directory as the prompt.

See also: https://docs.python.org/3/library/venv.html

Create a virtual environment, activate it on POSIX systems, and install `pytest`
```unix
$ python3 -m venv my_venv
$ source my_venv/bin/activate
(my_venv) ...$ pip install pytest
```
or using `virtualenv`
```unix
$ python3 -m pip install virtualenv
$ python3 -m virtualenv my_venv
$ source my_venv/bin/activate
(my_venv) ...$ pip install pytest
```
Deactivate the venv
```unix
(my_venv) ...$ deactivate
```
Create a virtual environment, activate it on Windows systems, and install `pytest`
```windows
>python -m venv my_venv
>my_venv\Scripts\activate.bat
(my_venv) ...>pip install pytest
```
Activate in PowerShell
```windows
>my_venv\Scripts\Activate.ps1
```

Install in editable mode from the current directory
```unix
(venv_editable) ...$ pip install -e .
```

Install in editable mode from a directory with optional dependencies for testing
```unix
(venv_editable) ...$ pip install -e "./cards_proj_failed/[test]"
```
`[test]` in the `-e` parameters refers to optional dependencies for testing given in `pyproject.toml`.

Other useful commands
```unix
(venv) ...$ pip --version
pip 24.2 from path/to/venv/lib/python3.11/site-packages/pip (python 3.11)
(venv) ...$ pip list
Package            Version
------------------ -----------
cachetools         5.5.0
cards              1.0.0
certifi            2024.8.30
...
```

See also: https://pip.pypa.io/en/stable/

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