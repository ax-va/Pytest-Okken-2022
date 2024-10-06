import hello


def test_say_hello(capsys):
    hello.say_hello()
    output = capsys.readouterr().out
    assert output == "Hello, World!\n"


"""
$ cd 12*/12-3*
$ pytest tests/test_hello.py
***
tests/test_hello.py .
***
$ cd ..
$ cd ..
"""