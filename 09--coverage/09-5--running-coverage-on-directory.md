# Coverage

## Running coverage on a directory

### Using Coverage.py at a path instead a package

Run pytest with a test directory
```unix
$ pytest --cov=09--coverage/some_code 09--coverage/some_code
***
Name                                       Stmts   Miss  Cover
--------------------------------------------------------------
09--coverage/some_code/bar_module.py           4      1    75%
09--coverage/some_code/foo_module.py           2      0   100%
09--coverage/some_code/test_some_code.py       6      0   100%
--------------------------------------------------------------
TOTAL                                         12      1    92%
***
```

Run pytest with a test file
```unix
$ pytest --cov=09--coverage/some_code 09--coverage/some_code/test_some_code.py
***
Name                                       Stmts   Miss  Cover
--------------------------------------------------------------
09--coverage/some_code/bar_module.py           4      1    75%
09--coverage/some_code/foo_module.py           2      0   100%
09--coverage/some_code/test_some_code.py       6      0   100%
--------------------------------------------------------------
TOTAL                                         12      1    92%
***
```