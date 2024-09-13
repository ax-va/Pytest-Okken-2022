## Install tox
```unix
$ pip install tox
```

## Run tox
```unix
$ cd cards_proj_tox
$ tox
py311: install_deps> python -I -m pip install faker pytest
***
py311: commands[0]> pytest
===================================================================================================== test session starts ======================================================================================================
platform linux -- Python 3.11.9, pytest-8.3.2, pluggy-1.5.0
cachedir: .tox/py311/.pytest_cache
rootdir: ***/cards_proj_tox
configfile: pytest.ini
testpaths: tests
plugins: Faker-28.4.1
collected 51 items                                                                                                                                                                                                             

tests/api/test_add.py .....                                                                                                                                                                                              [  9%]
tests/api/test_config.py .                                                                                                                                                                                               [ 11%]
tests/api/test_count.py ...                                                                                                                                                                                              [ 17%]
tests/api/test_delete.py ...                                                                                                                                                                                             [ 23%]
tests/api/test_finish.py ....                                                                                                                                                                                            [ 31%]
tests/api/test_list.py .........                                                                                                                                                                                         [ 49%]
tests/api/test_start.py ....                                                                                                                                                                                             [ 56%]
tests/api/test_update.py ....                                                                                                                                                                                            [ 64%]
tests/api/test_version.py .                                                                                                                                                                                              [ 66%]
tests/cli/test_add.py ..                                                                                                                                                                                                 [ 70%]
tests/cli/test_config.py ..                                                                                                                                                                                              [ 74%]
tests/cli/test_count.py .                                                                                                                                                                                                [ 76%]
tests/cli/test_delete.py .                                                                                                                                                                                               [ 78%]
tests/cli/test_errors.py .....                                                                                                                                                                                           [ 88%]
tests/cli/test_finish.py .                                                                                                                                                                                               [ 90%]
tests/cli/test_list.py ..                                                                                                                                                                                                [ 94%]
tests/cli/test_start.py .                                                                                                                                                                                                [ 96%]
tests/cli/test_update.py .                                                                                                                                                                                               [ 98%]
tests/cli/test_version.py .                                                                                                                                                                                              [100%]

====================================================================================================== 51 passed in 0.67s ======================================================================================================
***
  py311: OK (11.61=setup[10.21]+cmd[1.40] seconds)
  congratulations :) (11.69 seconds)
```