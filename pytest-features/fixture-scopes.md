- `scope='function'`: run once per test function, set as the default scope

- `scope='class'`: run once per test class, regardless of how many test methods are in the class

- `scope='module'`: run once per module, regardless of how many test functions or methods or other fixtures in the module use it

- `scope='package'`: run once per package, or test directory, regardless of how many test functions or methods or other fixtures in the package use it

- `scope='session'`: run once per session so that all test methods and functions using a fixture of session scope share one setup and teardown call