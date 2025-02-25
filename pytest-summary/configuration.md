# Configuration

## Root Directory

Once pytest finds a configuration file in a directory, it marks the directory as the root directory, or `rootdir`.
Therefore, the best practice is to place an empty configuration file at the top of a project, even if there aren't any configuration settings.
Otherwise, pytest will search to the root of the file system and can find one that has nothing to do with the project.

```unix
***/08--configuration-files$ pytest
platform linux -- Python 3.11.9, pytest-8.0.1, pluggy-1.4.0
rootdir: .../test_08--configuration-files
configfile: pytest.ini
plugins: Faker-24.11.0
collected 0 items
```

## Configuration Files

### `pytest.ini`

- changes pytest's default behavior. 

Its location also defines the pytest root directory, or `rootdir`.

### `conftest.py`

- contains *fixtures* and *hook functions* shared by all tests in the same directory or all subdirectories.

It can exist at the `rootdir` or in any subdirectory.

### `__init__.py`

- only to duplicate names of test files in different directories.

### `tox.ini`, `pyproject.toml`, `setup.cfg`

- take the place of `pytest.ini` for settings in one of these alternate configuration files.

## Example of a project directory structure

```
cards_proj
|---- <top level project files, src dir, docs, etc>
|---- pytest.ini
|---- tests
     |---- conftest.py
     |---- api
          |---- __init__.py
          |---- conftest.py
          |---- test_add.py  # Using duplicate test module names is only possible with `__init__.py`
          |---- <test files for API>
     |---- cli
          |---- __init__.py
          |---- conftest.py
          |---- test_add.py  # Using duplicate test module names is only possible with `__init__.py`
          |---- <test files for CLI>
```