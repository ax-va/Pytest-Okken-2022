## How to get available fixtures

List available fixtures
```unix
$ pytest --fixtures -v
...
------------------------------------------------------------------------------------------------ fixtures defined from conftest ------------------------------------------------------------------------------------------------
cards_db [session scope] -- test_examples/conftest.py:8
    CardsDB object connected to a temporary database 


--------------------------------------------------------------------------------------- fixtures defined from test_example-3-1--fixtures ---------------------------------------------------------------------------------------
some_data -- test_examples/test_example-3-1--fixtures.py:10
    Return answer to ultimate question 


-------------------------------------------------------------------------------- fixtures defined from test_example-3-3--fixtures--module-scope --------------------------------------------------------------------------------
cards_db [module scope] -- test_examples/test_example-3-3--fixtures--module-scope.py:8
    no docstring available


------------------------------------------------------------------------------ fixtures defined from test_example-3-2--fixtures--setup--teardown -------------------------------------------------------------------------------
cards_db -- test_examples/test_example-3-2--fixtures--setup--teardown.py:8
    no docstring available


==================================================================================================== no tests ran in 0.03s =====================================================================================================
```

List available fixtures in `test_examples`
```unix
$ pytest --fixtures -v test_examples
...
------------------------------------------------------------------------------------------------ fixtures defined from conftest ------------------------------------------------------------------------------------------------
cards_db [session scope] -- test_examples/conftest.py:8
    CardsDB object connected to a temporary database 


--------------------------------------------------------------------------------------- fixtures defined from test_example-3-1--fixtures ---------------------------------------------------------------------------------------
some_data -- test_examples/test_example-3-1--fixtures.py:10
    Return answer to ultimate question 


-------------------------------------------------------------------------------- fixtures defined from test_example-3-3--fixtures--module-scope --------------------------------------------------------------------------------
cards_db [module scope] -- test_examples/test_example-3-3--fixtures--module-scope.py:8
    no docstring available


------------------------------------------------------------------------------ fixtures defined from test_example-3-2--fixtures--setup--teardown -------------------------------------------------------------------------------
cards_db -- test_examples/test_example-3-2--fixtures--setup--teardown.py:8
    no docstring available


==================================================================================================== no tests ran in 0.03s =====================================================================================================
```

```unix
$ pytest --fixtures -v test_examples/test_example-3-1--fixtures.py
...
------------------------------------------------------------------------------------------------ fixtures defined from conftest ------------------------------------------------------------------------------------------------
cards_db [session scope] -- test_examples/conftest.py:8
    CardsDB object connected to a temporary database 


--------------------------------------------------------------------------------------- fixtures defined from test_example-3-1--fixtures ---------------------------------------------------------------------------------------
some_data -- test_examples/test_example-3-1--fixtures.py:10
    Return answer to ultimate question 


==================================================================================================== no tests ran in 0.01s =====================================================================================================
```

List fixtures used in a module
"""
$ pytest --fixtures-per-test -k test_example-3-4
...
------------------------------------------------------------------------------------------------- fixtures used by test_empty --------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------- (test_examples/test_example-3-4--fixtures--conftest_py.py:5) ---------------------------------------------------------------------------------
cards_db -- test_examples/conftest.py:8
    CardsDB object connected to a temporary database 

-------------------------------------------------------------------------------------------------- fixtures used by test_two ---------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------- (test_examples/test_example-3-4--fixtures--conftest_py.py:9) ---------------------------------------------------------------------------------
cards_db -- test_examples/conftest.py:8
    CardsDB object connected to a temporary database 

==================================================================================================== 25 deselected in 0.03s ====================================================================================================
"""

List fixtures used in a function
"""
$ pytest --fixtures-per-test test_examples/test_example-3-4--fixtures--conftest_py.py::test_empty
...
------------------------------------------------------------------------------------------------- fixtures used by test_empty --------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------- (test_examples/test_example-3-4--fixtures--conftest_py.py:5) ---------------------------------------------------------------------------------
cards_db -- test_examples/conftest.py:8
    CardsDB object connected to a temporary database 

==================================================================================================== no tests ran in 0.01s =====================================================================================================
"""