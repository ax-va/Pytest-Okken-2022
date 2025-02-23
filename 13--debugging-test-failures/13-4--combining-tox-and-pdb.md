# Debugging test failures

## Combining tox and pdb 

1. Run tox with pdb. (`--no-cov` turns off the coverage report.)

  ```unix
  (venv_editable)  .../cards_proj_failed$ tox -e py311 -- --pdb --no-cov
  ***
  tests/api/test_add.py .....                                                                                       [  9%]
  tests/api/test_config.py .                                                                                        [ 11%]
  tests/api/test_count.py ...                                                                                       [ 16%]
  tests/api/test_delete.py ...                                                                                      [ 22%]
  tests/api/test_finish.py ....                                                                                     [ 30%]
  tests/api/test_list.py .........                                                                                  [ 47%]
  tests/api/test_list_done.py .                                                                                     [ 49%]
  tests/api/test_start.py ....                                                                                      [ 56%]
  tests/api/test_update.py ....                                                                                     [ 64%]
  tests/api/test_version.py .                                                                                       [ 66%]
  tests/cli/test_add.py ..                                                                                          [ 69%]
  tests/cli/test_config.py ..                                                                                       [ 73%]
  tests/cli/test_count.py .                                                                                         [ 75%]
  tests/cli/test_delete.py .                                                                                        [ 77%]
  tests/cli/test_done.py F

  cards_db = <cards.api.CardsDB object at 0x7bd578713990>, cards_cli = <function cards_cli_no_redirect.<locals>.run_cli at 0x7bd5779113a0>

      def test_done(cards_db, cards_cli):
          cards_db.add_card(cards.Card("some task", state="done"))
          cards_db.add_card(cards.Card("another"))
          cards_db.add_card(cards.Card("a third", state="done"))
          output = cards_cli("done")
  >       assert output == expected
  E       AssertionError: assert '            ...      a third' == '\n  ID   sta...      a third'
  E         
  E         - 
  E         +                                   
  E             ID   state   owner   summary    
  E            ──────────────────────────────── 
  E             1    done            some task  
  E             3    done            a third
  
  tests/cli/test_done.py:16: AssertionError
  ***
  > ***/cards_proj_failed/tests/cli/test_done.py(16)test_done()
  -> assert output == expected
  (Pdb) ll
   11     def test_done(cards_db, cards_cli):
   12         cards_db.add_card(cards.Card("some task", state="done"))
   13         cards_db.add_card(cards.Card("another"))
   14         cards_db.add_card(cards.Card("a third", state="done"))
   15         output = cards_cli("done")
   16  ->     assert output == expected
  (Pdb) 
  ```

2. Look at `output` and `expected`.

  ```unix
  (Pdb) pp output
  ('                                  \n'
   '  ID   state   owner   summary    \n'
   ' ──────────────────────────────── \n'
   '  1    done            some task  \n'
   '  3    done            a third')
  (Pdb) pp expected
  ('\n'
   '  ID   state   owner   summary    \n'
   ' ──────────────────────────────── \n'
   '  1    done            some task  \n'
   '  3    done            a third')
  ```