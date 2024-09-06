## Setting tox

See `tox_covearge.ini`.

## Setting `.coveragerc`

Create a `.coveragerc` configuration file in `11-tox/cards_proj`
```
[paths]
source = 
   src
   .tox/*/lib/python*/site-packages
```

**tox** locates **cards** in its environments, for example, in `11-tox/cards_proj/.tox/py311/lib/python3.11/site-packages/cards`.
Then **Coverage.py** will check `.tox/py311/lib/python3.11/site-packages/cards`, but report it as `scr/cards`.

## Run tox choosing a specific environment
```unix
$ cd 11--tox/cards_proj
$ tox -c tox_coverage.ini -e py311
###
---------- coverage: platform linux, python 3.11.9-final-0 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
src/cards/__init__.py       3      0   100%
src/cards/api.py           72      0   100%
src/cards/cli.py           86      0   100%
src/cards/db.py            23      0   100%
-------------------------------------------
TOTAL                     184      0   100%
```