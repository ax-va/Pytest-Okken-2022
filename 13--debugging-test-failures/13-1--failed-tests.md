# Debugging test failures

## Prepare failures in `cards_project_failed`

1. Comment out `return done_cards` in `src.cards.api.CardsDB.list_done_cards`.

2. Comment out a correct value and comment in an incorrect value in `tests.cli.test_done`  

## Run pytest with turned-off tracebacks
```unix
(venv_editable)  ...$ cd cards_proj_failed
(venv_editable)  .../cards_proj_failed$ pytest --tb=no
*** 
tests/api/test_add.py .....                                                                                       [  9%]
tests/api/test_config.py .                                                                                        [ 11%]
tests/api/test_count.py ...                                                                                       [ 16%]
tests/api/test_delete.py ...                                                                                      [ 22%]
tests/api/test_finish.py ....                                                                                     [ 30%]
tests/api/test_list.py .........                                                                                  [ 47%]
tests/api/test_list_done.py F                                                                                     [ 49%]
tests/api/test_start.py ....                                                                                      [ 56%]
tests/api/test_update.py ....                                                                                     [ 64%]
tests/api/test_version.py .                                                                                       [ 66%]
tests/cli/test_add.py ..                                                                                          [ 69%]
tests/cli/test_config.py ..                                                                                       [ 73%]
tests/cli/test_count.py .                                                                                         [ 75%]
tests/cli/test_delete.py .                                                                                        [ 77%]
tests/cli/test_done.py F                                                                                          [ 79%]
tests/cli/test_errors.py .....                                                                                    [ 88%]
tests/cli/test_finish.py .                                                                                        [ 90%]
tests/cli/test_list.py ..                                                                                         [ 94%]
tests/cli/test_start.py .                                                                                         [ 96%]
tests/cli/test_update.py .                                                                                        [ 98%]
tests/cli/test_version.py .                                                                                       [100%]
***
FAILED tests/api/test_list_done.py::test_list_done - TypeError: object of type 'NoneType' has no len()
FAILED tests/cli/test_done.py::test_done - AssertionError: assert '' == '\n  ID   sta...      a third'
***
$ cd ..
```