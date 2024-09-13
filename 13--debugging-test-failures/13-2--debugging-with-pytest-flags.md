## Use `--lf` to re-run the failures only, and `--tb=no` to hide the traceback

```unix
(venv_editable)  .../cards_proj_failed$ pytest --lf --tb=no
***
run-last-failure: rerun previous 2 failures (skipped 19 files)

tests/api/test_list_done.py F                                                                                     [ 50%]
tests/cli/test_done.py F                                                                                          [100%]
***
FAILED tests/api/test_list_done.py::test_list_done - TypeError: object of type 'NoneType' has no len()
FAILED tests/cli/test_done.py::test_done - AssertionError: assert '' == '\n  ID   sta...      a third'
***
```

## Run the first failing test and stop after the failure

```unix
$ pytest --lf -x
***
run-last-failure: rerun previous 2 failures (skipped 19 files)

tests/api/test_list_done.py F
***
cards_db = <cards.api.CardsDB object at 0x78f22afe7ed0>

    @pytest.mark.num_cards(10)
    def test_list_done(cards_db):
        cards_db.finish(3)
        cards_db.finish(5)
    
        the_list = cards_db.list_done_cards()
    
>       assert len(the_list) == 2
E       TypeError: object of type 'NoneType' has no len()

tests/api/test_list_done.py:11: TypeError
***
FAILED tests/api/test_list_done.py::test_list_done - TypeError: object of type 'NoneType' has no len()
***
```

-> `the_list` is `None` instead of a (possibly empty) list of Card objects.

## Run the same test over again with `-l/--showlocals` and displaying local variables

```unix
$ pytest --lf -x -l --tb=short
***
run-last-failure: rerun previous 2 failures (skipped 19 files)

tests/api/test_list_done.py F
***
tests/api/test_list_done.py:11: in test_list_done
    assert len(the_list) == 2
E   TypeError: object of type 'NoneType' has no len()
        cards_db   = <cards.api.CardsDB object at 0x7ddff8121390>
        the_list   = None
***
FAILED tests/api/test_list_done.py::test_list_done - TypeError: object of type 'NoneType' has no len()
***
```

-> Use lots of intermediate variables in tests. They come in handy when a test fails.
