## How to run subsets of tests

| Subset                        | Syntax                                                 |
|-------------------------------|--------------------------------------------------------|
| Single test method            | `pytest <path>/test_module.py::TestClass::test_method` |
| All tests in a class          | `pytest <path>/test_module.py::TestClass`              |
| Single test function          | `pytest <path>/test_module.py::test_function`          |
| All tests in a module         | `pytest <path>/test_module.py`                         |
| All tests in a directory      | `pytest <path>`                                        |
| Tests matching a name pattern | `pytest -k <pattern>`                                  |
| Tests by marker               | separating out tests with build-in or custom markers   |

```unix
$ pytest -v -k TestEquality
===================================================================================================== test session starts ======================================================================================================
###
collected 20 items / 17 deselected / 3 selected                                                                                                                                                                                

test_02/test_02-7--classes.py::TestEquality::test_equality PASSED                                                                                                                                             [ 33%]
test_02/test_02-7--classes.py::TestEquality::test_equality_with_diff_ids PASSED                                                                                                                               [ 66%]
test_02/test_02-7--classes.py::TestEquality::test_inequality PASSED                                                                                                                                           [100%]

=============================================================================================== 3 passed, 17 deselected in 0.05s ===============================================================================================
```

```unix
$ pytest -v -k TestEq
===================================================================================================== test session starts ======================================================================================================
###
collected 20 items / 17 deselected / 3 selected                                                                                                                                                                                

test_02/test_02-7--classes.py::TestEquality::test_equality PASSED                                                                                                                                             [ 33%]
test_02/test_02-7--classes.py::TestEquality::test_equality_with_diff_ids PASSED                                                                                                                               [ 66%]
test_02/test_02-7--classes.py::TestEquality::test_inequality PASSED                                                                                                                                           [100%]

=============================================================================================== 3 passed, 17 deselected in 0.05s ===============================================================================================
```

```unix
$ pytest -v --tb=no -k equality
===================================================================================================== test session starts ======================================================================================================
###
collected 20 items / 13 deselected / 7 selected                                                                                                                                                                                

test_02/test_02-1--card.py::test_equality PASSED                                                                                                                                                              [ 14%]
test_02/test_02-1--card.py::test_equality_with_diff_ids PASSED                                                                                                                                                [ 28%]
test_02/test_02-1--card.py::test_inequality PASSED                                                                                                                                                            [ 42%]
test_02/test_02-2--card-fail.py::test_equality_fail FAILED                                                                                                                                                    [ 57%]
test_02/test_02-7--classes.py::TestEquality::test_equality PASSED                                                                                                                                             [ 71%]
test_02/test_02-7--classes.py::TestEquality::test_equality_with_diff_ids PASSED                                                                                                                               [ 85%]
test_02/test_02-7--classes.py::TestEquality::test_inequality PASSED                                                                                                                                           [100%]

=================================================================================================== short test summary info ====================================================================================================
FAILED test_02/test_02-2--card-fail.py::test_equality_fail - AssertionError: assert Card(summary=...odo', id=None) == Card(summary=...odo', id=None)
========================================================================================== 1 failed, 6 passed, 13 deselected in 0.06s ==========================================================================================
```

Eliminate the failing test
```unix
$ pytest -v --tb=no -k "equality and not equality_fail"
===================================================================================================== test session starts ======================================================================================================
###
collected 20 items / 14 deselected / 6 selected                                                                                                                                                                                

test_02/test_02-1--card.py::test_equality PASSED                                                                                                                                                              [ 16%]
test_02/test_02-1--card.py::test_equality_with_diff_ids PASSED                                                                                                                                                [ 33%]
test_02/test_02-1--card.py::test_inequality PASSED                                                                                                                                                            [ 50%]
test_02/test_02-7--classes.py::TestEquality::test_equality PASSED                                                                                                                                             [ 66%]
test_02/test_02-7--classes.py::TestEquality::test_equality_with_diff_ids PASSED                                                                                                                               [ 83%]
test_02/test_02-7--classes.py::TestEquality::test_inequality PASSED                                                                                                                                           [100%]

=============================================================================================== 6 passed, 14 deselected in 0.04s ===============================================================================================
```

Run of all tests with `dict` or `ids` in the name, but not ones in the `TestEquality` class
```unix
$ pytest -v --tb=no -k "(dict or ids) and not TestEquality"
===================================================================================================== test session starts ======================================================================================================
###
cachedir: .pytest_cache
###
collected 20 items / 16 deselected / 4 selected                                                                                                                                                                                

test_02/test_02-1--card.py::test_equality_with_diff_ids PASSED                                                                                                                                                [ 25%]
test_02/test_02-1--card.py::test_from_dict PASSED                                                                                                                                                             [ 50%]
test_02/test_02-1--card.py::test_to_dict PASSED                                                                                                                                                               [ 75%]
test_02/test_02-6--structure--given--when--then.py::test_to_dict PASSED                                                                                                                                                          [100%]

=============================================================================================== 4 passed, 16 deselected in 0.03s ===============================================================================================
```

Run all the tests with `test_05` in their names
```unix
$ pytest -v -k test_05
###
test_05--parametrization/test_05-1--motivation.py::test_finish_from_in_prog PASSED
test_05--parametrization/test_05-1--motivation.py::test_finish_from_done PASSED
test_05--parametrization/test_05-1--motivation.py::test_finish_from_todo PASSED
test_05--parametrization/test_05-1--motivation.py::test_finish PASSED
test_05--parametrization/test_05-2--function-parametrization.py::test_finish[write a book-done] PASSED
test_05--parametrization/test_05-2--function-parametrization.py::test_finish[second edition-in prog] PASSED
test_05--parametrization/test_05-2--function-parametrization.py::test_finish[create a course-todo] PASSED
test_05--parametrization/test_05-2--function-parametrization.py::test_finish_simple[done] PASSED
test_05--parametrization/test_05-2--function-parametrization.py::test_finish_simple[in prog] PASSED
test_05--parametrization/test_05-2--function-parametrization.py::test_finish_simple[todo] PASSED
test_05--parametrization/test_05-3--fixture-parametrization.py::test_finish[done] PASSED
test_05--parametrization/test_05-3--fixture-parametrization.py::test_finish[in prog] PASSED
test_05--parametrization/test_05-3--fixture-parametrization.py::test_finish[todo] PASSED
test_05--parametrization/test_05-4--pytest_generate_tests.py::test_finish[done] PASSED
test_05--parametrization/test_05-4--pytest_generate_tests.py::test_finish[in prog] PASSED
test_05--parametrization/test_05-4--pytest_generate_tests.py::test_finish[todo] PASSED
```

Run all the tests with `todo` pattern, also automatically with `todo` as the parameter value
```unix
$ pytest -v -k todo
###
test_05--parametrization/test_05-1--motivation.py::test_finish_from_todo PASSED
test_05--parametrization/test_05-2--function-parametrization.py::test_finish[create a course-todo] PASSED
test_05--parametrization/test_05-2--function-parametrization.py::test_finish_simple[todo] PASSED
test_05--parametrization/test_05-3--fixture-parametrization.py::test_finish[todo] PASSED
test_05--parametrization/test_05-4--pytest_generate_tests.py::test_finish[todo] PASSED  
###
```

Run all the tests with `todo` pattern, but not with `play` and not with `create`
```unix
$ pytest -v -k "todo and not (play or create)"
test_05--parametrization/test_05-1--motivation.py::test_finish_from_todo PASSED
test_05--parametrization/test_05-2--function-parametrization.py::test_finish_simple[todo] PASSED
test_05--parametrization/test_05-3--fixture-parametrization.py::test_finish[todo] PASSED
test_05--parametrization/test_05-4--pytest_generate_tests.py::test_finish[todo] PASSED
```