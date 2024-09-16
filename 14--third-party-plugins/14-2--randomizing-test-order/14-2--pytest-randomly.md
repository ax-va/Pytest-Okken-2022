Randomize the test run order to test for order independence. 
-> 
Use pytest-randomly.
It also randomizes the seed value for other random tools like Faker and Factory Boy.

Run tests normally
```unix
$ cd 14--third-party-plugins/14-2--randomizing-test-order
$ pytest -v
***
test_a.py::test_one PASSED                                                                                        [ 25%]
test_a.py::test_two PASSED                                                                                        [ 50%]
test_b.py::test_three PASSED                                                                                      [ 75%]
test_b.py::test_four PASSED                                                                                       [100%]
***
$ cd ..
$ cd .. 
```

Install pytest-randomly
```unix
$ pip install pytest-randomly
```

The tests are run randomly
```unix
$ cd 14--third-party-plugins/14-2--randomizing-test-order
$ pytest -v
***
test_b.py::test_four PASSED                                                                                       [ 25%]
test_b.py::test_three PASSED                                                                                      [ 50%]
test_a.py::test_two PASSED                                                                                        [ 75%]
test_a.py::test_one PASSED                                                                                        [100%]
***
$ cd ..
$ cd .. 
```

The tests are run randomly
```unix
$ cd 14--third-party-plugins/14-2--randomizing-test-order
$ pytest -v
***
test_b.py::test_four PASSED                                                                                       [ 25%]
test_b.py::test_three PASSED                                                                                      [ 50%]
test_a.py::test_one PASSED                                                                                        [ 75%]
test_a.py::test_two PASSED                                                                                        [100%]
***
$ cd ..
$ cd .. 
```