## Local conftest plugin

See the `local-conftest-plugin` directory.

## Used pytest hook functions 

Hook functions are entry points to intercept pytest behavior at certain points and make changes.

- `pytest_configure()` to perform initial configuration.

-> Users don't have to add the `slow` marker to the config file.

- `pytest_addoption()` to register options and settings.

-> The `--slow` flag is added by using this hook function.

- `pytest_collection_modifyitems()` to filter or re-order the test items after test collection has been performed.

-> It is used to find the slow tests and mark them for skipping.

See also:

- Pytest: hook functions

https://docs.pytest.org/en/latest/reference/reference.html#hook-reference

https://docs.pytest.org/en/6.2.x/writing_plugins.html#writinghooks