## New plugin should

1. Mark slow tests with `@pytest.mark.slow`, which should not always be run.
2. Add `@pytest.mark.skip(reason="need --slow option to run")` for the tests marked as `@pytest.mark.slow`.
3. Run all the tests (including the slow ones) with the `--slow` flag and skip the slow tests without this flag.
4. Run the only slow tests with the `-m slow --slow` flag.

| Behavior     | Without new plugin     | With new plugin         |
|--------------|------------------------|-------------------------|
| Exclude slow | `pytest -m "not slow"` | `pytest`                |
| Include slow | `pytest`               | `pytest --slow`         |
| Only slow    | `pytest -m slow`       | `pytest -m slow --slow` |

## Example without new plugin

```unix
$ cd 15--building-plugins/without-new-plugin
$ pytest -v -m "not slow"
***
collected 2 items / 1 deselected / 1 selected                                                                                                                                                                                  

test_slow.py::test_normal PASSED                                                                                  [100%]
***
$ cd ..
$ cd ..
```