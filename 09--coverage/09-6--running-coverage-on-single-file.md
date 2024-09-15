# Running coverage on a single file

Test functions are usually already included in a single file

```python
def foo():
    return "foo"


def bar():
    return "bar"


def baz():
    return "baz"


def main():
    print(foo(), baz())


if __name__ == "__main__":  # pragma: no cover
    main()

# test code, requires pytest


def test_foo():
    assert foo() == "foo"


def test_baz():
    assert baz() == "baz"


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "foo baz\n"
```

pytest with Coverage.py for a single file must be run in the same directory as the file.
Otherwise, Coverage.py cannot find imports of the module. 
```unix
$ pytest --cov=single_file 09--coverage/single_file.py
***
---------- coverage: platform linux, python 3.11.9-final-0 -----------
Name             Stmts   Miss  Cover
------------------------------------
single_file.py      16      1    94%
------------------------------------
TOTAL               16      1    94%
***
```

If we need to add parametrization or markers, we write tests in the `else` block
```python
if __name__ == '__main__': # pragma: no cover
    main()
else:
    import pytest
    ...
```