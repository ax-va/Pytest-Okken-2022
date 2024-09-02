# Running coverage on tests

## Motivation

- Checking for duplicate test function names

If we write new test functions with "copy/paste/modify", 
we can forget to change a function name, then only the last one in the file will be run.
In order to check, whether this problem occurs, we can add the test directory to the coverage.

- Checking for non-skipped tests and dead test code

This reports also make sure that all tests got run at least on some hardware and were not skipped.
This is possible because Coverage.py has the ability to combine reports from several test sessions.
Moreover, it also helps with finding unused fixtures, or dead code inside fixtures.

## Adding the test directory to the coverage
```unix
$ pytest --cov=cards --cov=07--test-strategies 07--test-strategies
###
---------- coverage: platform linux, python 3.11.9-final-0 -----------
Name                                        Stmts   Miss  Cover
---------------------------------------------------------------
07--test-strategies/tests/conftest.py          22      0   100%
07--test-strategies/tests/test_add.py          31      0   100%
07--test-strategies/tests/test_config.py        2      0   100%
07--test-strategies/tests/test_count.py         9      0   100%
07--test-strategies/tests/test_delete.py       28      0   100%
07--test-strategies/tests/test_finish.py       13      0   100%
07--test-strategies/tests/test_list.py         11      0   100%
07--test-strategies/tests/test_start.py        13      0   100%
07--test-strategies/tests/test_update.py       21      0   100%
07--test-strategies/tests/test_version.py       5      0   100%
cards_proj/src/cards/__init__.py                3      0   100%
cards_proj/src/cards/api.py                    70      3    96%
cards_proj/src/cards/cli.py                    86     53    38%
cards_proj/src/cards/db.py                     23      0   100%
---------------------------------------------------------------
TOTAL                                         337     56    83%
###
```