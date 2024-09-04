import hello


def test_hello(capsys):
    hello.hello()
    output = capsys.readouterr().out
    assert output == "Hello, World!\n"


"""
$ cd 12--testing-scripts-and-applications/12-2--testing-importable-python-script
$ pytest test_hello.py
###
test_hello.py .
###
"""