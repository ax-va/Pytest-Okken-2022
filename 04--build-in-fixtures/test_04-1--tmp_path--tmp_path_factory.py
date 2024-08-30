"""
The tmp_path function-scope fixture returns a pathlib.Path instance that points to a temporary directory.
The tmp_path_factory session-scope fixture returns a TempPathFactory
instance to use mktemp() to create multiple temporary directories.

The base directory for all the pytest temporary directory fixtures is system-and user-dependent,
and includes a pytest-<NUMBER> part, where <NUMBER> is incremented for every session.

Specify your own base directory with
$ pytest --basetemp=<MYDIR>
e.g.,
$ pytest --basetemp=04--build-in-fixtures/tmp -k=test_04

See also:
- tmpdir is similar to tmp_path, but returns a py.path.local instance (not recommended).
- mpdir_factory is similar to tmp_path_factory, except its mktemp function returns a py.path.local instance.
"""


def test_tmp_path(tmp_path):
    # tmp_path is function scope
    print(f"\ntype(tmp_path): {type(tmp_path)}")
    print(f"\nstr(tmp_path): {str(tmp_path)}")
    file = tmp_path / "file.txt"
    file.write_text("Hello")
    assert file.read_text() == "Hello"


def test_tmp_path_factory(tmp_path_factory):
    # tmp_path_factory is session scope
    print(f"\ntype(tmp_path_factory): {type(tmp_path_factory)}")
    print(f"\nstr(tmp_path_factory): {str(tmp_path_factory)}")
    # Call mktemp() to get a directory
    path = tmp_path_factory.mktemp("sub")
    file = path / "file.txt"
    file.write_text("Hello")
    assert file.read_text() == "Hello"

"""
$ pytest -k test_04-1 -s
===================================================================================================== test session starts ======================================================================================================
###                                                                                                                                                                              

04--build-in-fixtures/test_04-1--tmp_path--tmp_path_factory.py 
type(tmp_path): <class 'pathlib.PosixPath'>

str(tmp_path): /tmp/pytest-of-delorian/pytest-9/test_tmp_path0
.
type(tmp_path_factory): <class '_pytest.tmpdir.TempPathFactory'>

str(tmp_path_factory): TempPathFactory(_given_basetemp=None, _trace=<pluggy._tracing.TagTracerSub object at 0x7013536d9390>, _basetemp=PosixPath('/tmp/pytest-of-delorian/pytest-9'), _retention_count=3, _retention_policy='all')
.

=============================================================================================== 2 passed, 40 deselected in 0.04s ===============================================================================================
"""