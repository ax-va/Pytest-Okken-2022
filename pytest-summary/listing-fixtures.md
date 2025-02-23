# How to get available fixtures

List all the available fixtures
```unix
$ pytest --fixtures -v
```

List available fixtures in `03--fixtures`
```unix
$ pytest --fixtures -v 03--fixtures
```

List fixtures used in a module
```unix
$ pytest --fixtures -v 03--fixtures/a/test_03-1--fixtures.py
```

List fixtures used in a module
```unix
$ cd 03--fixtures
$ pytest --fixtures-per-test -k test_03-4
***
$ cd ..
```

List fixtures used in a function
```unix
$ pytest --fixtures-per-test 03--fixtures/a/test_03-4--conftest.py::test_empty
```