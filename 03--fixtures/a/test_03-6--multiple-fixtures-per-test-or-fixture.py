# multiple fixtures per test
def test_add_some(cards_db_empty, some_cards):
    expected_count = len(some_cards)
    for c in some_cards:
        cards_db_empty.add_card(c)
    assert cards_db_empty.count() == expected_count


def test_non_empty(cards_db_non_empty):
    assert cards_db_non_empty.count() > 0


"""
$ pytest 03--fixtures/a/test_03-6--multiple-fixtures-per-test-or-fixtures.py
***
03--fixtures/a/test_03-6--multiple-fixtures-per-test-or-fixture.py ..                                             [100%]
***
"""