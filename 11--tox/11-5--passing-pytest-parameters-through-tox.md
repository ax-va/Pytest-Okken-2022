## Settings

See the full settings in `tox_posargs.ini`.
Take into account this line `pytest --cov=cards --cov=tests --cov-fail-under=100 {posargs}`.
Then to pass arguments to pytest, add `--` between the tox arguments and the pytest arguments.

## Run tox with pytest arguments
```unix
$ cd cards_proj_tox
$ tox -c tox_posargs.ini -e py310 -- -k test_version --no-cov
###
tests/api/test_version.py .                                                                                       [ 50%]
tests/cli/test_version.py .                                                                                       [100%]
###
```
`--no-cov` is to turn off coverage.