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
07--test-strategies/tests/test_add.py .....                        [ 18%]
07--test-strategies/tests/test_config.py .                         [ 22%]
07--test-strategies/tests/test_count.py ...                        [ 33%]
07--test-strategies/tests/test_delete.py ...                       [ 44%]
07--test-strategies/tests/test_finish.py ....                      [ 59%]
07--test-strategies/tests/test_list.py ..                          [ 66%]
07--test-strategies/tests/test_start.py ....                       [ 81%]
07--test-strategies/tests/test_update.py ....                      [ 96%]
07--test-strategies/tests/test_version.py .                        [100%]

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
