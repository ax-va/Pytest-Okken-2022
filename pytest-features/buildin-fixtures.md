## Considered in `test_examples-04--buildin-fixtures`:

## `tmp_path`, `tmp_path_factory`

used to for temporary directories. 

`tmp_path` is function scope, and `tmp_path_factory` is session scope.

## `capsys`

used to capture `stdout` and `stderr`; also used to temporarily turn off output capture (to show `print`)

## `monkeypatch`

used to change the application code or the environment

## Not considered in `test_examples-04--buildin-fixtures`:

## `capfd`, `capfdbinary`, `capsysbinary`

variants of capsys that work with file descriptors and/or binary output

## `caplog`

similar to capsys and the like; used for messages created with Python’s logging system

## `cache`

used to store and retrieve values across pytest runs.

The most useful part of this fixture is that it allows for --last-failed, --failed-first, and similar flags.

## `doctest_namespace`

useful if you like to use pytest to run doctest-style tests

## `pytestconfig`

used to get access to configuration values, `pluginmanager`, and plugin hooks

## `record_property`, `record_testsuite_property`

used to add extra properties to the test or test suite. 

Especially useful for adding data to an XML report to be used by continuous integration tools.

## `recwarn`

used to test warning messages

## `request`

used to provide information on the executing test function. 

Most commonly used during fixture parametrization.

## `pytester`, `testdir`

used to provide a temporary test directory to aid in running and testing pytest plugins; `pathlib.Path` for `pytester` and `py.path.local` for `testdir`

## `tmpdir`, `tmpdir_factory`

similar to `tmp_path` and `tmp_path_factory`; used to return a `py.path.local` object instead of a `pathlib.Path` object

Show all available fixtures including the build-in fixtures

```unix
$ pytest --fixtures
```
