## The Cards application

https://github.com/okken/cards

External dependencies for Cards are defined in its `pyproject.toml` file.

## Install the application code stored locally
```unix
(venv) $ pip install ./cards_proj/
```

## Install the application with new features in editable mode and with its dependencies

Editable mode is needed in `13--debugging-test-failures`.
Editable mode refers to a way of installing a Python package such that any changes 
you make to the source code are immediately reflected without needing to reinstall the package.

```unix
(venv_editable) $ pip install -e "./cards_proj_failed/[test]"
```

`[test]` in the `-e` parameters refers to optional dependencies for testing given in `pyproject.toml`.

```tolm
[project.optional-dependencies]
test = [
    "pytest",
    "faker",
    "tox",
    "coverage",
    "pytest-cov",
]
```

The `cards_proj_failed` source code contains new features, 
namely `list_done_cards` for API and CLI that causes testing failures.

## Play with the application (under test)

```unix
$ cards version
1.0.0
```

```unix
$ python -i
>>> import cards
>>> cards.__version__
'1.0.0'
```

```unix
$ cards --help
Usage: cards [OPTIONS] COMMAND [ARGS]...

  Cards is a small command line task tracking application.

Options:
  --help  Show this message and exit.

Commands:
  add      Add a card to db.
  config   List the path to the Cards db.
  count    Return number of cards in db.
  delete   Remove card in db with given id.
  finish   Set a card state to 'done'.
  list     List cards in db.
  start    Set a card state to 'in prog'.
  update   Modify a card in db with given id with new info.
  version  Return version of cards application
```

CLI examples:

```unix
$ cards add do something --owner ax-va
$ cards add do something else
                                     
  ID   state   owner   summary       
 ─────────────────────────────────── 
  1    todo    ax-va   do something  

$ cards add do something --owner Brian
$ cards
                                     
  ID   state   owner   summary       
 ─────────────────────────────────── 
  1    todo    ax-va   do something  
  2    todo    Brian   do something  

$ cards start 1cards start 1
$ cards
                                       
  ID   state     owner   summary       
 ───────────────────────────────────── 
  1    in prog   ax-va   do something  
  2    todo      Brian   do something  
                                       
$ cards finish 1
$ cards start 2
                                       
  ID   state     owner   summary       
 ───────────────────────────────────── 
  1    done      ax-va   do something  
  2    in prog   Brian   do something  

$ cards delete 1   

  ID   state     owner   summary       
 ───────────────────────────────────── 
  2    in prog   Brian   do something  
     
$ cards add do something else
$ cards  

  ID   state     owner   summary            
 ────────────────────────────────────────── 
  2    in prog   Brian   do something       
  3    todo              do something else  

$ cards update 2 --owner NoName

  ID   state     owner    summary            
 ─────────────────────────────────────────── 
  2    in prog   NoName   do something       
  3    todo               do something else  

$ cards count
2
```                              

## The Cards source code consists of three layers: CLI, API, and DB

The API is implemented in `api.py`.

The CLI is implemented in `cli.py` with the dependency on two third-party packages:
- Typer https://pypi.org/project/typer/
- Rich https://pypi.org/project/rich/

The interaction with the database is implemented in `db.py` with the dependency on one third-party package:
- TinyDB https://pypi.org/project/tinydb/

The CLI and database layers are as thin as possible. 