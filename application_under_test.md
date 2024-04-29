## Install the application code stored locally
```unix
(venv) $ pip install ./cards_proj/
```

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

CLI: `cards`, `cards add`, `cards update`, `cards start`, `cards finish`, and `cards delete`

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

## The Cards source code consists of three layers: CLI, API, and DB.

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

The CLI is implemented in `cli.py`. It depends on two third-party packages:
- Typer https://pypi.org/project/typer/
- Rich https://pypi.org/project/rich/
