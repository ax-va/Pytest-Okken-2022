## Root directory

Once pytest finds a configuration file in a directory, it marks the directory as the root directory, or `rootdir`.
Therefore, the best practice is to place an empty `pytest.ini` at the top of a project, even if there aren't any configuration settings.
Otherwise, pytest will search to the root of the file system and can find one that has nothing to do with the project.

```unix
.../07--configuration-files$ pytest
platform linux -- Python 3.11.9, pytest-8.0.1, pluggy-1.4.0
rootdir: .../test_07--configuration-files
configfile: pytest.ini
plugins: Faker-24.11.0
collected 0 items
```

## Configuration files

- `pytest.ini`

changes pytest's default behavior. 
Its location also defines the pytest root directory, or `rootdir`.

- `conftest.py`

contains fixtures and hook functions.
It can exist at the `rootdir` or in any subdirectory.
Anything defined in `conftest.py` applies to tests in that directory and all subdirectories.

- `__init__.py`

only to have duplicated names of test files.

- `tox.ini`, `pyproject.toml`, and `setup.cfg`

take the place of `pytest.ini` for settings in one of these alternate configuration files.

## Example project directory structure
```
cards_proj
|---- <top level project files, src dir, docs, etc>
|---- pytest.ini
|---- tests
     |---- conftest.py
     |---- api
          |---- __init__.py
          |---- conftest.py
          |---- test_add.py  # Using duplicated names is only possible with `__init__.py`
          |---- <test files for API>
     |---- cli
          |---- __init__.py
          |---- conftest.py
          |---- test_add.py  # Using duplicated names is only possible with `__init__.py`
          |---- <test files for CLI>
```