## Different ways to launch pdb from pytest in commandline

- Add a `breakpoint()` call to either test code or application code.

- Use the `--pdb` flag. Then, pytest will stop at the point of failure.

- Use the `--trace` flag. Then, pytest will stop at the beginning of each test function.

## Debugging in IPython

- `pytest --lf --trace --pdbcls=IPython.terminal.debugger:TerminalPdb`

- `pytest --pdb --pdbcls=IPython.terminal.debugger:TerminalPdb`

- Put `breakpoint()` in the sourcecode and run `pytest --pdbcls=IPython.terminal.debugger:TerminalPdb`

## Debug with pdb in commandline

1. Combine the `--lf` and `--trace` flags to run the last failed tests 
and stop at the beginning of the first failed one.

```unix
(venv_editable)  .../cards_proj_failed$ pytest --lf --trace
***
run-last-failure: rerun previous 2 failures (skipped 19 files)

tests/api/test_list_done.py 
***
> ***/cards_proj_failed/tests/api/test_list_done.py(6)test_list_done()
-> cards_db.finish(3)
(Pdb) 
```

2. List the source code of the current function.

```unix
(Pdb) ll
  4     @pytest.mark.num_cards(10)
  5     def test_list_done(cards_db):
  6  ->     cards_db.finish(3)
  7         cards_db.finish(5)
  8     
  9         the_list = cards_db.list_done_cards()
 10     
 11         assert len(the_list) == 2
 12         for card in the_list:
 13             assert card.id in (3, 5)
 14             assert card.state == "done"
(Pdb) 
```

The `->` shows the current line, before it's been run.

3. Continue running until line 8.

```unix
(Pdb) until 8
> ***/cards_proj_failed/tests/api/test_list_done.py(9)test_list_done()
-> the_list = cards_db.list_done_cards()
(Pdb) 
```

4. Go into the function.

```unix
(Pdb) step
--Call--
> ***/cards_proj_failed/src/cards/api.py(91)list_done_cards()
-> def list_done_cards(self):
(Pdb) 
```

5. See the whole function.

```unix
(Pdb) ll
 91  ->     def list_done_cards(self):
 92             """Return the 'done' cards."""
 93             done_cards = self.list_cards(state="done")
(Pdb) 
```

6. Continue and go the last line of the function.

```unix
(Pdb) r
--Return--
> ***/cards_proj_failed/src/cards/api.py(93)list_done_cards()->None
-> done_cards = self.list_cards(state="done")
(Pdb) 
```

7. List the source code of the function again.

```unix
(Pdb) ll
 91         def list_done_cards(self):
 92             """Return the 'done' cards."""
 93  ->         done_cards = self.list_cards(state="done")
(Pdb) 
```

8. Look at the value of `done_cards` with either `p` or `pp`.

```unix
(Pdb) pp done_cards
[Card(summary='Line for PM identify decade.',
      owner='Russell',
      state='done',
      id=3),
 Card(summary='Director baby season industry the describe.',
      owner='Cody',
      state='done',
      id=5)]
(Pdb) 
```

(The problem: `done_cards` is not returned.)

9. Continue out to the calling test and check the return value.

```unix
(Pdb) step
> ***/cards_proj_failed/tests/api/test_list_done.py(11)test_list_done()
-> assert len(the_list) == 2
(Pdb) ll
  4     @pytest.mark.num_cards(10)
  5     def test_list_done(cards_db):
  6         cards_db.finish(3)
  7         cards_db.finish(5)
  8     
  9         the_list = cards_db.list_done_cards()
 10     
 11  ->     assert len(the_list) == 2
 12         for card in the_list:
 13             assert card.id in (3, 5)
 14             assert card.state == "done"
(Pdb) pp the_list
None
(Pdb) 
```

10. Stop the debugger.
```unix
(Pdb) exit
```

Add `return done_cards` in `api.CardsDB.list_done_cards` and re-run tests.

```unix
$ pytest --lf -x -v --tb=no
***
run-last-failure: rerun previous 2 failures (skipped 19 files)

tests/api/test_list_done.py::test_list_done PASSED                                                                [ 50%]
tests/cli/test_done.py::test_done FAILED                                                                          [100%]
***
```