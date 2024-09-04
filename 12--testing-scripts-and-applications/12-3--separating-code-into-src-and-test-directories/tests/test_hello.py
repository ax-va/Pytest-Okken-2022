import hello


def test_hello(capsys):
    hello.hello()
    output = capsys.readouterr().out
    assert output == "Hello, World!\n"


"""
$ cd 12--testing-scripts-and-applications/12-3--separating-code-into-src-and-test-directories
$ pytest tests/test_hello.py
###
tests/test_hello.py .
###
"""