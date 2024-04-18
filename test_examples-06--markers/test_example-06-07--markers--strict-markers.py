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
$ pytest -m smoke
###
### PytestUnknownMarkWarning: Unknown pytest.mark.smok - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.smok

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
###
"""

# Run without --strict-markers
"""
$ pytest -k test_example-06-07
###
### PytestUnknownMarkWarning: Unknown pytest.mark.smok - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.smok

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
###
"""

# Run with --strict-markers to change warnings to errors
"""
$ pytest --strict-markers -m smok
###
### ERROR collecting test_example-06-07--markers--strict-markers.py
###
### Failed: 'smok' not found in `markers` configuration option
###
"""
# 1) The error is issued at collection time, not at run time.
# 2) Errors are sometimes easier to catch than warnings, especially in continuous integration systems.

# Recommended to add "--strict-markers" into pytest.ini
"""
[pytest]
markers =
    smoke: subset of tests
    exception: check for expected exceptions
addopts =
    --strict-markers
"""