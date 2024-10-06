Use AND
```unix
$ cd 06*
$ pytest -m "smoke and exception" -v
###
test_06-05--markers--custom-markers--files--classes--parameters.py::test_finish_non_existent PASSED
###
$ cd ..
```

Use OR
```unix
$ cd 06*
$ pytest -m "smoke or exception" -v
***
test_06-04--markers--custom-markers.py::test_start PASSED
test_06-04--markers--custom-markers.py::test_start_non_existent PASSED
test_06-05--markers--custom-markers--files--classes--parameters.py::test_finish_non_existent PASSED
***
$ cd ..
```

Use NOT
```unix
$ cd 06*
$ pytest -m "smoke and not exception" -v
***
test_06-04--markers--custom-markers.py::test_start PASSED
***
$ cd ..
```

Use parentheses
```unix
$ cd 06*
$ pytest -m "(smoke or smoke1) and exception" -v
***
test_06-05--markers--custom-markers--files--classes--parameters.py::test_finish_non_existent PASSED
***
$ cd ..
```

Combine markers and keywords for selection
```unix
$ cd 06*
$ pytest -v -m smoke -k "not TestFinish"
***
test_06-04--markers--custom-markers.py::test_start PASSED
test_06-05--markers--custom-markers--files--classes--parameters.py::test_finish_non_existent PASSED
***
$ cd ..
```

Non-strict matching for keywords
```unix
$ cd 06*
$ pytest -v -m smoke -k "not TestFin"
***
test_06-04--markers--custom-markers.py::test_start PASSED
test_06-05--markers--custom-markers--files--classes--parameters.py::test_finish_non_existent PASSED
***
$ cd ..
```

But strict matching for markers
```unix
$ cd 06*
$ pytest -v -m smok -k "not TestFin"
***
*** 0 selected
***
$ cd ..
```