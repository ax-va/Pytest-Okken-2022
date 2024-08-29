"""
The capsys fixture enables the capturing of writes to stdout and stderr.
Also, "with capsys.disabled():" disables normal output capturing without using the -s or --capture=no flags.

See also:

- capfd
is like capsys, but captures file descriptors 1 and 2, which usually is the same as stdout and stderr.

- capsysbinary
capsys captures text, capsysbinary captures bytes.

- capfdbinary
captures bytes on file descriptors 1 and 2.

- caplog
captures output written with the logging package.
"""
import cards

# Motivation 1: test the command-line output
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
    # capsys.readouterr() returns a namedtuple that has out and err
    output = capsys.readouterr().out.rstrip()  # rstrip() to remove the newline
    assert output == cards.__version__


# Motivation 2:
# The output is not displayed, because pytest captures all the outputs.
# To show print(), use the -s or --capture=no flags in the command line.
def test_normal():
    print("\nnormal print")


# However, print() is displayed in a failing test.
def test_fail():
    print("\nprint in failing test")
    assert False


# Alternatively, disable capturing to display print() without using additional flags.
def test_disabled(capsys):
    with capsys.disabled():
        print("\ncapsys disabled print")
