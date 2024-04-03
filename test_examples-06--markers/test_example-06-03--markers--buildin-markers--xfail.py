"""
@pytest.mark.xfail(condition, ..., *, reason, run=True, raises=None, strict=xfail_strict)

Short description:
run=False       don't run
raises          sets an exception type or a tuple of exception types that you want to result in an xfail
strict          should be marked as XPASS (strict=False) or FAIL (strict=True) when passing

Global setting:
xfail_strict=true in pytest.ini

Reasons to mark with xfail:
- Test-driven development for non-implemented behaviors yet but planed to be implemented shortly.
- Remember you if a behavior is fixed with xfail, strict=True.

Result meaning when failing
XFAIL           "You were right, it did fail"

Result meaning when passing
XPASS           "Good news, the test you thought would fail just passed"
FAILED          "You thought it would fail, but it didn’t. You were wrong."
"""
import pytest
import cards
from packaging.version import parse  # third-party package
from cards import Card


@pytest.mark.xfail(
    parse(cards.__version__).major < 2,  # optional condition parameter
    reason="Card < comparison not supported in 1.x",
)
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2


@pytest.mark.xfail(reason="XPASS demo with strict=False")
def test_xpass():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2


@pytest.mark.xfail(
    reason="FAILED demo with strict=True",
    strict=True,
)
def test_xfail_strict():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2


"""
$ pytest -k example-06-03 -v -ra
...
test_examples-06--markers/test_example-06-03--markers--buildin-markers--xfail.py::test_less_than XFAIL (Card < comparison not supported in 1.x) 
test_examples-06--markers/test_example-06-03--markers--buildin-markers--xfail.py::test_xpass XPASS (XPASS demo with strict=False)  
test_examples-06--markers/test_example-06-03--markers--buildin-markers--xfail.py::test_xfail_strict FAILED 
...
=================================================================================================== short test summary info ====================================================================================================
XFAIL test_examples-06--markers/test_example-06-03--markers--buildin-markers--xfail.py::test_less_than - Card < comparison not supported in 1.x
XPASS test_examples-06--markers/test_example-06-03--markers--buildin-markers--xfail.py::test_xpass - XPASS demo with strict=False
FAILED test_examples-06--markers/test_example-06-03--markers--buildin-markers--xfail.py::test_xfail_strict
...
"""