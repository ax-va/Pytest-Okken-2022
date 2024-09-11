# Commandline flags 

## Useful flags

- `-c`: to use configuration file.

- `-l`, `--showlocals`: to display local variables alongside the stacktrace.

- `-k <pattern>`: to match a name pattern of tests (`k` for keyword).

- `-ra`: `-r` for reporting reasons for test results at the end of the session; `a` for "all except passed".

- `-rfE`: `-r` for reporting reasons for test results at the end of the session; `f` for failed tests; `E` for errors.

- `-s`, `--capture=no`: to turn off output capture -> to show `print`s not only for failed tests.

- `-v`, `--verbose`: to dDisplays all the test names, passing or failing.

- `-vv`: to show all mismatches in a test.

- `--basetemp=<mydir>`: to specify your own base directory.

- `--fixtures -v`: to show a list of all available fixtures; `-v` for the entire docstring.

- `--help`: to show help.

- `--setup-show`: to show the order of operations of tests and fixtures, including the setup and teardown phases.

- `--strict-markers`: to change warnings on misspelled markers to errors.

- `--tb=[auto/long/short/line/native/no]`: to control displaying tracebacks.

- `--tb=no`: to turn off tracebacks.

- `--tb=short`: to use the shorter traceback format.


## Flags to select which tests to run, in which order, and when to stop

- `lf`, `--last-failed`: to run the tests that failed last.

- `-ff`, `--failed-first`: to run all the tests, starting with the last failed.

- `-x`, `--exitfirst`: to stop the tests session after the first failure.

- `--maxfail=num`: to stop the tests after `num` failures.

- `-nf`, `--new-first`: to runs all the tests, ordered by file modification time.

- `--sw`, `--stepwise`: to stop the tests at the first failure and to start the tests at the last failure next time.

- `--sw-skip`, `--stepwise-skip`: same as `--sw`, but with skipping the first failure.


## Flags to start a commandline debugger

- `--pdb`: to start an interactive debugging session at the point of failure.

- `--trace`: to start the pdb source-code debugger immediately when running each test.

- `--pdbcls`: to use alternatives to pdb, such as IPython's debugger with `--pdbcls=IPython.terminal.debugger:TerminalPdb`
