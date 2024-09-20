# Testing the plugin with pytester

## Installable plugin with pytester

See `15--building-plugins/installable-plugin-with-pytester`.

## Pytester

pytester creates a temporary directory for each test with the `pytester` fixture.

Helpful functions to populate this directory:

- `makefile()` to create any file.

- `makepyfile()` to create a Python (commonly test) file.

- `makeconftest()` to create `conftest.py`

- `makeini()` to creates `tox.ini`.

- `makepyprojecttoml()` to create `pyproject.toml`.

- `maketxtfile()` to create a txt file.

- `mkdir()` and `mkpydir()` to create test subdirectories with or without `__init__.py`, respectively.

- `copy_example()` to copy files from the project's directory to the temporary directory.

See also: 

- pytester

https://docs.pytest.org/en/latest/reference/reference.html#std-fixture-pytester

## runpytest()

See `15--building-plugins/installable-plugin-with-pytester/tests/test_plugin.py`.

See also:

- RunResult

https://docs.pytest.org/en/latest/reference/reference.html#pytest.RunResult

Install the plugin in editable mode.
```unix
(venv_plugin) ***$ cd 15--building-plugins/installable-plugin-with-pytester
(venv_plugin) ***$ pip uninstall pytest-skip-slow-by-ax-va
(venv_plugin) ***$ pip install -e .
```

Run plugin tests.
```unix
$ pytest -v tests/test_plugin.py
***
tests/test_plugin.py::test_skip_slow PASSED                                                                       [ 25%]
tests/test_plugin.py::test_run_slow PASSED                                                                        [ 50%]
tests/test_plugin.py::test_run_only_slow PASSED                                                                   [ 75%]
tests/test_plugin.py::test_help PASSED                                                                            [100%]
***
```
