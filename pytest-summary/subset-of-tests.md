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

Run tests using the `-k` flag
```unix
$ pytest -v -k TestEquality
```

```unix
$ pytest -v -k TestEq
```

```unix
$ pytest -v --tb=no -k equality
```

```unix
$ pytest -v --tb=no -k "equality and not equality_fail"
```

Run of all tests with `dict` or `ids` in the name, but not ones in the `TestEquality` class
```unix
$ pytest -v --tb=no -k "(dict or ids) and not TestEquality"
```

Run all the tests with `test_05` in their names
```unix
$ pytest -v -k test_05
```

Run all the tests with `todo` pattern, also automatically with `todo` as the parameter value
```unix
$ pytest -v -k todo
###
05--parametrization/test_05-1--motivation.py::test_finish_from_todo PASSED
05--parametrization/test_05-2--function-parametrization.py::test_finish[create a course-todo] PASSED
05--parametrization/test_05-2--function-parametrization.py::test_finish_simple[todo] PASSED
05--parametrization/test_05-3--fixture-parametrization.py::test_finish[todo] PASSED
05--parametrization/test_05-4--pytest_generate_tests.py::test_finish[todo] PASSED  
###
```

Run all the tests with `todo` pattern, but not with `play` and not with `create`
```unix
$ pytest -v -k "todo and not (play or create)"
05--parametrization/test_05-1--motivation.py::test_finish_from_todo PASSED
05--parametrization/test_05-2--function-parametrization.py::test_finish_simple[todo] PASSED
05--parametrization/test_05-3--fixture-parametrization.py::test_finish[todo] PASSED
05--parametrization/test_05-4--pytest_generate_tests.py::test_finish[todo] PASSED
```