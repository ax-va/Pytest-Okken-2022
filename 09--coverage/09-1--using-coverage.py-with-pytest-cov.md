# Using Coverage.py with pytest-cov

## Coverage.py
A preferred Python coverage tool that measures code coverage

https://coverage.readthedocs.io/en/

```unix
$ pip install coverage
```

## pytest-cov
A popular pytest plugin often used in conjunction with coverage.py

https://pytest-cov.readthedocs.io/en/latest/

```unix
$ pip install pytest-cov
```

## The `--cov` flag

Run tests with the `--cov` flag, specifying either a path to code to test or an installed package to test

```unix
$ pytest --cov=cards 07--test-strategies
###
07--test-strategies/tests/test_add.py .....                                                                       [ 18%]
07--test-strategies/tests/test_config.py .                                                                        [ 22%]
07--test-strategies/tests/test_count.py ...                                                                       [ 33%]
07--test-strategies/tests/test_delete.py ...                                                                      [ 44%]
07--test-strategies/tests/test_finish.py ....                                                                     [ 59%]
07--test-strategies/tests/test_list.py ..                                                                         [ 66%]
07--test-strategies/tests/test_start.py ....                                                                      [ 81%]
07--test-strategies/tests/test_update.py ....                                                                     [ 96%]
07--test-strategies/tests/test_version.py .                                                                       [100%]

---------- coverage: platform linux, python 3.11.9-final-0 -----------
Name                                                  Stmts   Miss  Cover
-------------------------------------------------------------------------
venv/lib/python3.11/site-packages/cards/__init__.py       3      0   100%
venv/lib/python3.11/site-packages/cards/api.py           70      3    96%
venv/lib/python3.11/site-packages/cards/cli.py           86     53    38%
venv/lib/python3.11/site-packages/cards/db.py            23      0   100%
-------------------------------------------------------------------------
TOTAL                                                   182     56    69%

###
```
100% coverage means that the test suite is hitting every line in those files.
The `cli.py` file is at 38% coverage because it was imported by `__init__.py` 
but the content of the functions were not run.

## Coverage.py without pytest-cov
```unix
$ coverage run --source=cards -m pytest 07--test-strategies
###
07--test-strategies/tests/test_add.py .....                                                                       [ 18%]
07--test-strategies/tests/test_config.py .                                                                        [ 22%]
07--test-strategies/tests/test_count.py ...                                                                       [ 33%]
07--test-strategies/tests/test_delete.py ...                                                                      [ 44%]
07--test-strategies/tests/test_finish.py ....                                                                     [ 59%]
07--test-strategies/tests/test_list.py ..                                                                         [ 66%]
07--test-strategies/tests/test_start.py ....                                                                      [ 81%]
07--test-strategies/tests/test_update.py ....                                                                     [ 96%]
07--test-strategies/tests/test_version.py .                                                                       [100%]
###
```
```unix
$ coverage report
Name                                                  Stmts   Miss  Cover
-------------------------------------------------------------------------
venv/lib/python3.11/site-packages/cards/__init__.py       3      0   100%
venv/lib/python3.11/site-packages/cards/api.py           70      3    96%
venv/lib/python3.11/site-packages/cards/cli.py           86     53    38%
venv/lib/python3.11/site-packages/cards/db.py            23      0   100%
-------------------------------------------------------------------------
TOTAL                                                   182     56    69%
```

## Coverage.py configuration

Create a `.coverarge` configuration file
```
[paths]
source =
    cards_proj/src/cards
    */site-packages/cards
```

Then Coverage.py will treat the `cards_proj/src/cards` directory as if it's the same 
as the installed cards within `*/site-packages/cards`.

```unix
###
07--test-strategies/tests/test_add.py .....                                                                       [ 18%]
07--test-strategies/tests/test_config.py .                                                                        [ 22%]
07--test-strategies/tests/test_count.py ...                                                                       [ 33%]
07--test-strategies/tests/test_delete.py ...                                                                      [ 44%]
07--test-strategies/tests/test_finish.py ....                                                                     [ 59%]
07--test-strategies/tests/test_list.py ..                                                                         [ 66%]
07--test-strategies/tests/test_start.py ....                                                                      [ 81%]
07--test-strategies/tests/test_update.py ....                                                                     [ 96%]
07--test-strategies/tests/test_version.py .                                                                       [100%]

---------- coverage: platform linux, python 3.11.9-final-0 -----------
Name                               Stmts   Miss  Cover
------------------------------------------------------
cards_proj/src/cards/__init__.py       3      0   100%
cards_proj/src/cards/api.py           70      3    96%
cards_proj/src/cards/cli.py           86     53    38%
cards_proj/src/cards/db.py            23      0   100%
------------------------------------------------------
TOTAL                                182     56    69%
###
```
The report lists the local files with shorter paths instead of the installed package location.

## Missing lines

Add missing lines to the terminal report
```unix
$ pytest --cov=cards --cov-report=term-missing 07--test-strategies
###
Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
cards_proj/src/cards/__init__.py       3      0   100%
cards_proj/src/cards/api.py           70      3    96%   72, 78, 82
cards_proj/src/cards/cli.py           86     53    38%   20, 28-30, 36-40, 51-63, 73-80, 86-90, 96-100, 106-107, 113-114, 122-123, 127-132, 137-140
cards_proj/src/cards/db.py            23      0   100%
----------------------------------------------------------------
TOTAL                                182     56    69%
####
```

Alternatively
```unix
$ coverage report --show-missing
Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
cards_proj/src/cards/__init__.py       3      0   100%
cards_proj/src/cards/api.py           70      3    96%   72, 78, 82
cards_proj/src/cards/cli.py           86     53    38%   20, 28-30, 36-40, 51-63, 73-80, 86-90, 96-100, 106-107, 113-114, 122-123, 127-132, 137-140
cards_proj/src/cards/db.py            23      0   100%
----------------------------------------------------------------
TOTAL                                182     56    69%
```