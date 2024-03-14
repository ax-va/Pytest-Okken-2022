from cards import Card


class TestEquality:
    def test_equality(self):
        c1 = Card("something", "brian", "todo", 123)
        c2 = Card("something", "brian", "todo", 123)
        assert c1 == c2

    def test_equality_with_diff_ids(self):
        c1 = Card("something", "brian", "todo", 123)
        c2 = Card("something", "brian", "todo", 4567)
        assert c1 == c2

    def test_inequality(self):
        c1 = Card("something", "brian", "todo", 123)
        c2 = Card("completely different", "okken", "done", 123)
        assert c1 != c2


# Run all the tests in the class
"""
$ pytest -v test_examples-02/test_example-02-7--classes.py::TestEquality
===================================================================================================== test session starts ======================================================================================================
...
collected 3 items                                                                                                                                                                                                              

test_examples-02/test_example-02-7--classes.py::TestEquality::test_equality PASSED                                                                                                                                             [ 33%]
test_examples-02/test_example-02-7--classes.py::TestEquality::test_equality_with_diff_ids PASSED                                                                                                                               [ 66%]
test_examples-02/test_example-02-7--classes.py::TestEquality::test_inequality PASSED                                                                                                                                           [100%]

====================================================================================================== 3 passed in 0.03s =======================================================================================================
"""

# Run a single test in the class
"""
$ pytest -v test_examples-02/test_example-02-7--classes.py::TestEquality::test_equality
===================================================================================================== test session starts ======================================================================================================
...
collected 1 item                                                                                                                                                                                                               

test_examples-02/test_example-02-7--classes.py::TestEquality::test_equality PASSED                                                                                                                                             [100%]

====================================================================================================== 1 passed in 0.03s =======================================================================================================
"""