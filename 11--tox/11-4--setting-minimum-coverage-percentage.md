## Settings

See the full settings in `tox_coverage_mini.ini`.
Take into account this line `commands = pytest --cov=cards --cov=tests --cov-fail-under=100`.

## Run tox
```unix
$ cd cards_proj_tox
$ tox -c tox_coverage_min.ini -e py310
***
---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name                        Stmts   Miss  Cover
-----------------------------------------------
src/cards/__init__.py           3      0   100%
src/cards/api.py               72      0   100%
src/cards/cli.py               86      0   100%
src/cards/db.py                23      0   100%
tests/api/__init__.py           0      0   100%
tests/api/test_add.py          30      0   100%
tests/api/test_config.py        2      0   100%
tests/api/test_count.py         9      0   100%
tests/api/test_delete.py       28      0   100%
tests/api/test_finish.py       13      0   100%
tests/api/test_list.py         26      0   100%
tests/api/test_start.py        13      0   100%
tests/api/test_update.py       21      0   100%
tests/api/test_version.py       5      0   100%
tests/cli/__init__.py           0      0   100%
tests/cli/conftest.py          17      0   100%
tests/cli/test_add.py          13      0   100%
tests/cli/test_config.py        5      0   100%
tests/cli/test_count.py         4      0   100%
tests/cli/test_delete.py        5      0   100%
tests/cli/test_errors.py        8      0   100%
tests/cli/test_finish.py        6      0   100%
tests/cli/test_list.py         12      0   100%
tests/cli/test_start.py         6      0   100%
tests/cli/test_update.py        7      0   100%
tests/cli/test_version.py       3      0   100%
tests/conftest.py              22      0   100%
-----------------------------------------------
TOTAL                         439      0   100%

Required test coverage of 100% reached. Total coverage: 100.00%
***
$ cd ..
```