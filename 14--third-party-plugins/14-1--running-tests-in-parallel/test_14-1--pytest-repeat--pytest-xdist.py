"""
See also the `--looponfail` flag of pytest-xdist to re-run the previously failing tests
in a loop after each file change until they pass after which again a full run is performed.
->
This can be useful for debugging a bunch of test failures.
"""
import time


def test_something():
    time.sleep(1)


"""
$ cd 14--third-party-plugins/14-1--running-tests-in-parallel
$ pytest -k test_14-1
***
collected 1 item

test_14-1--pytest-repeat--pytest-xdist.py .                                                                       [100%]
***
*** 1 passed in 1.03s ***
$ cd ..
$ cd ..
"""

# Run it 10 times with the `--count=10` parameter (pytest-repeat installed)
"""
$ cd 14--third-party-plugins/14-1--running-tests-in-parallel
$ pytest --count=10 -k test_14-1
***
collected 10 items

test_14-1--pytest-repeat--pytest-xdist.py ..........                                                              [100%]
***
*** 10 passed in 10.06s ***
$ cd ..
$ cd ..
"""

# Run 10 tests in parallel on 4 CPUs with `-n=4` (pytest-xdist installed)
"""
$ cd 14--third-party-plugins/14-1--running-tests-in-parallel
$ pytest --count=10 -n=4 -k test_14-1
***
4 workers [10 items]
..........                                                                                                        [100%]
*** 10 passed in 3.54s ***
$ cd ..
$ cd ..
"""

# Use `-n=auto` (the best practice) to run on as many CPU cores as possible
"""
$ cd 14--third-party-plugins/14-1--running-tests-in-parallel
$ pytest --count=10 -n=auto -k test_14-1
***
8 workers [10 items]
..........                                                                                                        [100%]
*** 10 passed in 2.76s ***
$ cd ..
$ cd ..
"""

# Run 8 tests in parallel on 8 CPUs
"""
$ cd 14--third-party-plugins/14-1--running-tests-in-parallel
$ pytest --count=8 -n=8 -k test_14-1
***
8 workers [8 items]
........                                                                                                          [100%]
*** 8 passed in 1.76s ***
$ cd ..
$ cd ..
"""

# Run 80 tests in parallel on 8 CPUs
"""
$ cd 14--third-party-plugins/14-1--running-tests-in-parallel
$ pytest --count=80 -n=8 -k test_14-1
***
8 workers [80 items]
................................................................................                                  [100%]
*** 80 passed in 10.80s ***
$ cd ..
$ cd ..
"""
# The overhead grew a little with 10 times the tests, from 0.76 seconds to 0.80 seconds.
