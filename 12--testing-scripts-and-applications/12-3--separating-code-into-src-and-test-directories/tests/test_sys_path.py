import sys


def test_sys_path():
    print("\nsys.path: ")
    for p in sys.path:
        print(p)


"""
$ cd 12*/12-3*
$ pytest -s tests/test_sys_path.py
tests/test_sys_path.py 
sys.path: 
***/12--testing-scripts-and-applications/12-3--separating-code-into-src-and-test-directories/tests
***/12--testing-scripts-and-applications/12-3--separating-code-into-src-and-test-directories/src
***
***/venv/lib/python3.11/site-packages
.
***
$ cd ..
$ cd ..
"""