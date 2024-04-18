## How to get available fixtures

List all the available fixtures
```unix
$ pytest --fixtures -v
###
------------------------------------------------------------------------------------------------ fixtures defined from conftest ------------------------------------------------------------------------------------------------
cards_db [session scope] -- test_examples-03--fixtures/conftest.py:8
    CardsDB object connected to a temporary database 


--------------------------------------------------------------------------------------- fixtures defined from test_example-03-1--fixtures ---------------------------------------------------------------------------------------
some_data -- test_examples-03--fixtures/test_example-03-1--fixtures.py:10
    Return answer to ultimate question 


-------------------------------------------------------------------------------- fixtures defined from test_example-03-3--fixtures--module-scope --------------------------------------------------------------------------------
cards_db [module scope] -- test_examples-03--fixtures/test_example-03-3--fixtures--module-scope.py:8
    no docstring available


------------------------------------------------------------------------------ fixtures defined from test_example-03-2--fixtures--setup--teardown -------------------------------------------------------------------------------
cards_db -- test_examples-03--fixtures/test_example-03-2--fixtures--setup--teardown.py:8
    no docstring available


###

==================================================================================================== no tests ran in 0.03s =====================================================================================================
```

List available fixtures in `test_examples-03--fixtures`
```unix
$ pytest --fixtures -v test_examples-03--fixtures
###
------------------------------------------------------------------------------------------------ fixtures defined from conftest ------------------------------------------------------------------------------------------------
cards_db [session scope] -- test_examples-03--fixtures/conftest.py:8
    CardsDB object connected to a temporary database 


--------------------------------------------------------------------------------------- fixtures defined from test_example-03-1--fixtures ---------------------------------------------------------------------------------------
some_data -- test_examples-03--fixtures/test_example-03-1--fixtures.py:10
    Return answer to ultimate question 


-------------------------------------------------------------------------------- fixtures defined from test_example-03-3--fixtures--module-scope --------------------------------------------------------------------------------
cards_db [module scope] -- test_examples-03--fixtures/test_example-03-3--fixtures--module-scope.py:8
    no docstring available


------------------------------------------------------------------------------ fixtures defined from test_example-03-2--fixtures--setup--teardown -------------------------------------------------------------------------------
cards_db -- test_examples-03--fixtures/test_example-03-2--fixtures--setup--teardown.py:8
    no docstring available


###

==================================================================================================== no tests ran in 0.03s =====================================================================================================
```

```unix
$ pytest --fixtures -v test_examples-03--fixtures/test_example-03-1--fixtures.py
###
------------------------------------------------------------------------------------------------ fixtures defined from conftest ------------------------------------------------------------------------------------------------
cards_db [session scope] -- test_examples-03--fixtures/conftest.py:8
    CardsDB object connected to a temporary database 


--------------------------------------------------------------------------------------- fixtures defined from test_example-03-1--fixtures ---------------------------------------------------------------------------------------
some_data -- test_examples-03--fixtures/test_example-03-1--fixtures.py:10
    Return answer to ultimate question 


==================================================================================================== no tests ran in 0.01s =====================================================================================================
```

List fixtures used in a module
```unix
$ pytest --fixtures-per-test -k test_example-03-4
===================================================================================================== test session starts ======================================================================================================
###                                                                                                                                                                             

------------------------------------------------------------------------------------------------- fixtures used by test_empty --------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------- (test_examples-03--fixtures/test_example-03-4--fixtures--conftest.py:5) ------------------------------------------------------------------------------
cards_db -- test_examples-03--fixtures/conftest.py:8
    CardsDB object connected to a temporary database 

-------------------------------------------------------------------------------------------------- fixtures used by test_two ---------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------- (test_examples-03--fixtures/test_example-03-4--fixtures--conftest.py:9) ------------------------------------------------------------------------------
cards_db -- test_examples-03--fixtures/conftest.py:8
    CardsDB object connected to a temporary database 

==================================================================================================== 29 deselected in 0.03s ====================================================================================================
```

List fixtures used in a function
```unix
$ pytest --fixtures-per-test test_examples-03--fixtures/test_example-03-4--fixtures--conftest.py::test_empty
===================================================================================================== test session starts ======================================================================================================
###                                                                                                                                                                                                          

------------------------------------------------------------------------------------------------- fixtures used by test_empty --------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------- (test_examples-03--fixtures/test_example-03-4--fixtures--conftest.py:5) ------------------------------------------------------------------------------
cards_db -- test_examples-03--fixtures/conftest.py:8
    CardsDB object connected to a temporary database 

==================================================================================================== no tests ran in 0.01s =====================================================================================================
```