"""
How to test outputs to stdout, stderr, and so on.
The capsys fixture enables the capturing of writes to stdout and stderr.
Also, it can disable normal output capture from pytest by using the -s or --capture=no flags.
"""
import cards

# Motivation: test the command-line output:
# $ cards version
# 1.0.0
import subprocess


def test_version_v1():
    process = subprocess.run(
        ["cards", "version"],
        capture_output=True,
        text=True
    )
    output = process.stdout.rstrip()  # rstrip() to remove the newline
    assert output == cards.__version__


def test_version_v2(capsys):
    cards.cli.version()
    # The capsys.readouterr() method returns a namedtuple that has out and err
    output = capsys.readouterr().out.rstrip()
    assert output == cards.__version__


def test_normal():
    # We don't see the output, because pytest captures all the outputs
    print("\nnormal print")
