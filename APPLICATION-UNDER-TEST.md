## The Cards application

https://github.com/okken/cards

External dependencies for Cards are defined in its `pyproject.toml` file.

## Install the application code stored locally
```unix
(venv) $ pip install ./cards_proj/
```

## Install the application with new features in editable mode and its dependencies

```unix
(venv_cards_editable) $ pip install -e "./cards_proj_tox_ext/[test]"
```

where `[tests]` refers to optional dependencies for testing specified in `pyproject.toml` as

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

**Editable mode** refers to a way of installing a Python package such that any changes 
you make to the source code are immediately reflected without needing to reinstall the package.
We need editable mode with extended in the chapter 13.
The `cards_proj_ext` source code also contains new `list_done_cards` for API and CLI.

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

## `cards_proj/src/cards/api.py`

``` python
@dataclass
class Card:
    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, d):
        return Card(**d)
        
    def to_dict(self):
        return asdict(self)
```

## Return the database location
``` unix
$ cards config
/home/delorian/cards_db
```

## Redirect the CLI to a temporary directory for the database
``` python
def get_path():
    db_path_env = os.getenv("CARDS_DB_DIR", "")
    if db_path_env:
        db_path = pathlib.Path(db_path_env)
    else:
        db_path = pathlib.Path.home() / "cards_db"
    return db_path
```

## Implementation of the API, CLI and database layers

The API is implemented in `api.py`.

The CLI is implemented in `cli.py` with the dependency on two third-party packages:
- Typer https://pypi.org/project/typer/
- Rich https://pypi.org/project/rich/

The interaction with the database is implemented in `db.py` with the dependency on one third-party package:
- TinyDB https://pypi.org/project/tinydb/

The CLI and database layers are as thin as possible. 