## Test Outcomes

- `PASSED`, `.`: ran and successful

- `FAILED`, `F`: ran and not successful

- `SKIPPED`, `s`: skipped, skip with the `@pytest.mark.skip()` or `@pytest.mark.skipif()` decorators

- `XFAIL` `x`: not supposed to pass, ran, and failed, mark with the `@pytest.mark.xfail()` decorator

- `XPASS`, `X`: marked with `xfail`, but ran and passed

- `ERROR`, `E`: an exception was raised either during the execution of a fixture or hook function, and not during the execution of a test function
