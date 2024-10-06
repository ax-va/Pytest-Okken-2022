import hello


def test_say_hello(capsys):
    hello.say_hello()
    output = capsys.readouterr().out
    assert output == "Hello, World!\n"


"""
$ cd 12*/12-2*
$ pytest test_hello.py
***
test_hello.py .
***
$ cd ..
$ cd ..
"""