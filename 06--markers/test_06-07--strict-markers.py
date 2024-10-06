import pytest
from cards import InvalidCardId


# Misspell "smoke" as "smok"
@pytest.mark.smok
@pytest.mark.exception
def test_start_non_existent(cards_db):
    """
    Shouldn't be able to start a non-existent card.
    """
    any_number = 123  # index is invalid
    with pytest.raises(InvalidCardId):
        cards_db.start(any_number)


# Run without --strict-markers
"""
$ cd 06*
$ pytest -m smoke
***
*** PytestUnknownMarkWarning: Unknown pytest.mark.smok - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.smok

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
***
$ cd ..
"""

# Run without --strict-markers
"""
$ cd 06*
$ pytest -k test_06-07
***
*** PytestUnknownMarkWarning: Unknown pytest.mark.smok - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.smok

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
***
$ cd ..
"""

# Run with --strict-markers to change warnings to errors
"""
$ cd 06*
$ pytest --strict-markers -m smok
***
*** ERROR collecting test_06-07--strict-markers.py
***
*** Failed: 'smok' not found in `markers` configuration option
***
$ cd ..
"""
# 1) The error is issued at collection time, not at run time.
# 2) Errors are sometimes easier to catch than warnings, especially in continuous integration systems.

# Recommended to add "--strict-markers" into pytest.ini
"""
[pytest]
addopts =
    --strict-markers

markers =
    smoke: subset of tests
    exception: check for expected exceptions
"""