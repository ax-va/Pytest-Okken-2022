"""
Test the rest of the CLI.

A "monkey patch" is a dynamic modification of a class or module during runtime.

The monkeypatch builtin fixture allows you to replace either input dependencies
or output dependencies in the context of a single test modifying objects,
dictionaries, environment variables, the python search path, or the current directory.

The monkeypatch fixture provides the following functions:
- setattr(target, name, value, raising=True)        sets an attribute
- delattr(target, name, raising=True)               deletes an attribute
- setitem(dic, name, value)                         sets a dictionary entry
- delitem(dic, name, raising=True)                  deletes a dictionary entry
- setenv(name, value, prepend=None)                 sets an environment variable
- delenv(name, raising=True)                        deletes an environment variable
- syspath_prepend(path)                             prepends path to sys.path, which is Python’s list of import locations
- chdir(path)                                       changes the current working directory

raising=True => raise an exception if the item doesn't already exist

tmp_path is also a build-in fixture and is function scope.
"""
import cards
from typer.testing import CliRunner


# Preparation
def test_version_v3():
    runner = CliRunner()
    result = runner.invoke(cards.app, ["version"])
    output = result.output.rstrip()
    assert output == cards.__version__


def run_cards(*params):
    """
    Helper function
    """
    runner = CliRunner()
    result = runner.invoke(cards.app, params)
    return result.output.rstrip()


def test_run_cards():
    """
    Test the help function
    """
    assert run_cards("version") == cards.__version__


# Monkey-patching
def test_patch_get_path(monkeypatch, tmp_path):
    # Replace the get_path function that is an attribute of cards.cli
    monkeypatch.setattr(cards.cli, "get_path", lambda: tmp_path)
    assert run_cards("config") == str(tmp_path)


def test_patch_home(monkeypatch, tmp_path):
    full_cards_dir = tmp_path / "cards_db"
    # Replace the home() method in cards.cli.pathlib.Path
    monkeypatch.setattr(cards.cli.pathlib.Path, "home", lambda: tmp_path)
    assert run_cards("config") == str(full_cards_dir)


def test_patch_env_var(monkeypatch, tmp_path):
    monkeypatch.setenv("CARDS_DB_DIR", str(tmp_path))
    assert run_cards("config") == str(tmp_path)


"""
$ pytest -k test_04-3
===================================================================================================== test session starts ======================================================================================================
***                                                                                                                                                                               

04--build-in-fixtures/test_04-3--monkeypatch.py .....                                                                                                                             [100%]

=============================================================================================== 5 passed, 44 deselected in 0.07s ===============================================================================================
"""