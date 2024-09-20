"""
A pytest plugin to skip `@pytest.mark.slow` tests by default.
Include the slow tests with `--slow`.
"""
import pytest

__version__ = "0.0.1"


def pytest_configure(config):
    # Users don't have to add the `slow` marker to the config file
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_addoption(parser):
    # The `--slow` flag is added by using this hook function
    parser.addoption(
        "--slow",
        # Store a `true` in the slow configuration
        # setting when the `--slow` flag is passed in,
        # and `false` otherwise.
        action="store_true",
        # Create a line in the `help` output to describe the flag:
        # $ cd 15--building-plugins/local-conftest-plugin
        # $ pytest --help
        # ***
        # Custom options:
        # ***
        #   --slow                include tests marked slow
        # ***
        help="include tests marked slow",
    )


def pytest_collection_modifyitems(config, items):
    # Get the slow setting by using
    # `config.getoption("slow")` or `config.getoption("--slow")`.
    if not config.getoption("--slow"):
        # Find the slow tests and mark them for skipping
        skip_slow = pytest.mark.skip(reason="need --slow option to run")
        # Iterate the list of Node objects
        for item in items:
            # Return either a marker object if there is a `slow` marker on the test or None
            if item.get_closest_marker("slow"):
                # Add the skip marker
                item.add_marker(skip_slow)
