Use AND
```unix
$ pytest -m "smoke and exception" -v
...
test_example-06-05--markers--custom-markers--files--classes--parameters.py::test_finish_non_existent PASSED
...
```

Use OR
```unix
$ pytest -m "smoke or exception" -v
...
test_example-06-04--markers--custom-markers.py::test_start PASSED
test_example-06-04--markers--custom-markers.py::test_start_non_existent PASSED
test_example-06-05--markers--custom-markers--files--classes--parameters.py::test_finish_non_existent PASSED
...
```

Use NOT
```unix
$ pytest -m "smoke and not exception" -v
...
test_example-06-04--markers--custom-markers.py::test_start PASSED
...
```

Use parentheses
```unix
$ pytest -m "(smoke or smoke1) and exception" -v
...
test_example-06-05--markers--custom-markers--files--classes--parameters.py::test_finish_non_existent PASSED
...
```

Combine markers and keywords for selection
```unix
$ pytest -v -m smoke -k "not TestFinish"
...
test_example-06-04--markers--custom-markers.py::test_start PASSED
test_example-06-05--markers--custom-markers--files--classes--parameters.py::test_finish_non_existent PASSED
...
```

Non-strict matching for keywords
```unix
$ pytest -v -m smoke -k "not TestFin"
...
test_example-06-04--markers--custom-markers.py::test_start PASSED
test_example-06-05--markers--custom-markers--files--classes--parameters.py::test_finish_non_existent PASSED
...
```

But strict matching for keywords
```unix
$ pytest -v -m smok -k "not TestFin"
...
... 0 selected
...
```