# multiple fixtures per test
def test_add_some(empty_db, some_cards):
    expected_count = len(some_cards)
    for c in some_cards:
        empty_db.add_card(c)
    assert empty_db.count() == expected_count


def test_non_empty(non_empty_db):
    assert non_empty_db.count() > 0


"""
$ pytest -k test_example-03-6
===================================================================================================== test session starts ======================================================================================================
###                                                                                                                                                                               

test_examples-03--fixtures--multiple-fixtures-per-test-or-fixture/test_example-03-6--fixtures--multiple-fixtures-per-test-or-fixture.py ..                                                                                   [100%]

=============================================================================================== 2 passed, 30 deselected in 0.06s ===============================================================================================
("""