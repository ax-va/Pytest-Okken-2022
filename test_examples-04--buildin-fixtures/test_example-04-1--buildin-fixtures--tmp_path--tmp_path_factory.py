"""
The tmp_path function-scope fixture returns a pathlib.Path instance that points to a temporary directory.
The tmp_path_factory session-scope fixture returns a TempPathFactory instance to use mktemp() to create
multiple temporary directories.
The base directory for all the pytest temporary directory fixtures is system-and user-dependent,
and includes a pytest-NUM part, where NUM is incremented for every session.
Specify your own base directory with
$ pytest --basetemp=mydir.
"""
import logging

logger = logging.getLogger(__name__)


def test_tmp_path(tmp_path):
    # tmp_path is function scope
    logger.info(f"type(tmp_path): {type(tmp_path)}")
    logger.info(f"str(tmp_path): {str(tmp_path)}")
    file = tmp_path / "file.txt"
    file.write_text("Hello")
    assert file.read_text() == "Hello"


def test_tmp_path_factory(tmp_path_factory):
    # tmp_path_factory is session scope
    logger.info(f"type(tmp_path_factory): {type(tmp_path_factory)}")
    logger.info(f"str(tmp_path_factory): {str(tmp_path_factory)}")
    # Call mktemp() to get a directory
    path = tmp_path_factory.mktemp("sub")
    file = path / "file.txt"
    file.write_text("Hello")
    assert file.read_text() == "Hello"


"""
See also:
- tmpdir is similar to tmp_path, but returns a py.path.local instance (not recommended).
- mpdir_factory is similar to tmp_path_factory, except its mktemp function returns a py.path.local instance.
"""

"""
$ pytest -k test_example-04-1 -c test_examples-04--buildin-fixtures/pytest.ini
===================================================================================================== test session starts ======================================================================================================
...
configfile: pyproject.toml
collected 39 items / 37 deselected / 2 selected                                                                                                                                                                                

test_examples-04--buildin-fixtures/test_example-04-1--buildin-fixtures--tmp_path--tmp_path_factory.py::test_tmp_path 
-------------------------------------------------------------------------------------------------------- live log call ---------------------------------------------------------------------------------------------------------
2024-03-19 18:53:50 [    INFO] type(tmp_path): <class 'pathlib.PosixPath'> (test_example-04-1--buildin-fixtures--tmp_path--tmp_path_factory.py:17)
2024-03-19 18:53:50 [    INFO] str(tmp_path): /tmp/pytest-of-delorian/pytest-1/test_tmp_path0 (test_example-04-1--buildin-fixtures--tmp_path--tmp_path_factory.py:18)
PASSED                                                                                                                                                                                                                   [ 50%]
test_examples-04--buildin-fixtures/test_example-04-1--buildin-fixtures--tmp_path--tmp_path_factory.py::test_tmp_path_factory 
-------------------------------------------------------------------------------------------------------- live log call ---------------------------------------------------------------------------------------------------------
2024-03-19 18:53:50 [    INFO] type(tmp_path_factory): <class '_pytest.tmpdir.TempPathFactory'> (test_example-04-1--buildin-fixtures--tmp_path--tmp_path_factory.py:26)
2024-03-19 18:53:50 [    INFO] str(tmp_path_factory): TempPathFactory(_given_basetemp=None, _trace=<pluggy._tracing.TagTracerSub object at 0x736a86ad88d0>, _basetemp=PosixPath('/tmp/pytest-of-delorian/pytest-1'), _retention_count=3, _retention_policy='all') (test_example-04-1--buildin-fixtures--tmp_path--tmp_path_factory.py:27)
PASSED                                                                                                                                                                                                                   [100%]

=============================================================================================== 2 passed, 37 deselected in 0.05s ===============================================================================================
"""