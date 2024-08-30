## Build-In Markers

- `@pytest.mark.filterwarnings(warning)` adds a warning filter to the given test.

- `@pytest.mark.skip(reason=None)` skips the test with an optional reason.

- `@pytest.mark.skipif(condition, ..., *, reason)` skips the test if any of the conditions are `True`.

- `@pytest.mark.xfail(condition, ..., *, reason, run=True, raises=None, strict=xfail_strict)` tells pytest that we expect the test to fail.

- `@pytest.mark.parametrize(argnames, argvalues, indirect, ids, scope)` calls a test function multiple times, passing in different arguments in turn.

- `@pytest.mark.usefixtures(fixturename1, fixturename2, ...)` marks tests as needing all the specified fixtures.
