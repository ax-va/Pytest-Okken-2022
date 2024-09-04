import typer
from typing import Optional

app = typer.Typer()


def full_output(name: str):
    return f"Hello, {name}!"


@app.command()
def say_hello(name: Optional[str] = typer.Argument("World")):
    print(full_output(name))


if __name__ == "__main__":
    app()


"""
$ cd 12--testing-scripts-and-applications
$ cd 12-4--testing-requirements-txt-based-applications
$ python src/hello.py
Hello, World!
$ python src/hello.py Alex
Hello, Alex!
"""