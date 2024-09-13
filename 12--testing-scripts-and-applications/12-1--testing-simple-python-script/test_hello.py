"""
Questions
1. how to run `hello.py` from a test?
2. how to capture the output?
->
Use Python's `subprocess.run`.

See also:
- Python's `subprocess.run`
https://docs.python.org/3/library/subprocess.html#subprocess.run
"""
from subprocess import run


def test_hello():
    result = run(
        ["python", "hello.py"],
        capture_output=True,
        text=True,
    )
    output = result.stdout
    assert output == "Hello, World!\n"


# Test
"""
$ cd 12--testing-scripts-and-applications/12-1--testing-simple-python-script
$ pytest -s -v test_hello.py
***
test_hello.py::test_hello PASSED
***
"""

# Test by using tox
"""
$ cd 12--testing-scripts-and-applications/12-1--testing-simple-python-script
$ tox
***
  py310: OK (0.32=setup[0.04]+cmd[0.28] seconds)
  py311: OK (0.27=setup[0.01]+cmd[0.27] seconds)
  congratulations :) (0.66 seconds)
***
"""