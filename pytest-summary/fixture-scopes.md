# Fixture Scopes 

Fixtures can only depend on other fixtures of their same scope or wider.

Tests can use any fixture that is in the same test module as a test function, or in a `conftest.py` file in the same directory, or in any level of parent directory up to the root of the tests.


### `scope='function'`

- Run once per test function, set as the default scope.

### `scope='class'`

- Run once per test class, regardless of how many test methods are in the class.

### `scope='module'`

- Run once per module, regardless of how many test functions or methods or other fixtures in the module use it.

### `scope='package'`

- Run once per package, or test directory, regardless of how many test functions or methods or other fixtures in the package use it.

### `scope='session'`

- Run once per session so that all test methods and functions using a fixture of session scope share one setup and teardown call.