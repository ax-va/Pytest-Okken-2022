# Building plugins

## Creating the installable plugin

### Plugin source code

Plugin source code is placed in the `installable-plugin` directory.
```
installable-plugin
|-- examples
|   |-- test_slow.py
|-- pytest_skip_slow_by_ax_va.py
```

The content of `conftest.py` is moved into `pytest_skip_slow.py`.
The tests in the `examples` subdirectory will be used to test the plugin itself.

### Creating a package with Flit

Flit creates `pyproject.toml` and optionally the `LICENSE` file.

```unix
$ pip install flit
$ cd 15--building-plugins/installable-plugin
$ flit init
Module name [pytest_skip_slow]: pytest-skip-slow-by-ax-va       
Author: ax-va
Author email: <my_email>
Home page: https://github.com/ax-va/Pytest-Okken-2022
Choose a license (see http://choosealicense.com/ for more info)
1. MIT - simple and permissive
2. Apache - explicitly grants patent rights
3. GPL - ensures that code based on this is shared with the same terms
4. Skip - choose a license later
Enter 1-4: 1

Written pyproject.toml; edit that file to add optional extra info.
```

Now, `pyproject.toml` and `LICENSE` have been added to the subdirectory.
```
installable-plugin
|-- examples
|   |-- test_slow.py
|-- LICENSE
|-- pyproject.toml
|-- pytest_skip_slow_by_ax_va.py
```

Modify `pyproject.toml` and add `README.md`.
```toml
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "pytest-skip-slow-by-ax-va"
authors = [{name = "ax-va", email = "<my_email>"}]
readme = "README.md"
license = {file = "LICENSE"}
classifiers = [
    "License :: OSI Approved :: MIT License",
    "Framework :: Pytest"
]
dynamic = ["version", "description"]
dependencies = ["pytest>=8.0.1"]
requires-python = ">=3.11"

[project.urls]
Home = "https://github.com/ax-va/Pytest-Okken-2022"

[project.entry-points.pytest11]
# Must be of the form:
# name_of_plugin = "plugin_module"
skip_slow_by_ax_va = "pytest_skip_slow_by_ax_va"

[project.optional-dependencies]
# Install tox when installing the package in editable mode
test = ["tox"]

[tool.flit.module]
# actual name of module
name = "pytest_skip_slow_by_ax_va"
```

See also:

- Pytest: Making your plugin installable by others

https://docs.pytest.org/en/latest/how-to/writing_plugins.html#making-your-plugin-installable-by-others

- Flit: `pyproject.toml`

https://flit.pypa.io/en/latest/pyproject_toml.html

Build an installable package.
```unix
$ flit build
***
Built sdist: dist/pytest_skip_slow_by_ax_va-0.0.1.tar.gz                                               I-flit_core.sdist
***
Built wheel: dist/pytest_skip_slow_by_ax_va-0.0.1-py3-none-any.whl                                     I-flit_core.wheel
```

Install the plugin from wheel.
```unix
(venv_plugin) ***$ pip install dist/pytest_skip_slow_by_ax_va-0.0.1-py3-none-any.whl
```

Test the installed plugin.
```unix
(venv_plugin) ***$ pytest examples/test_slow.py
examples/test_slow.py .s                                                                                          [100%]
(venv_plugin) ***$ pytest --slow examples/test_slow.py
examples/test_slow.py ..                                                                                          [100%]
(venv_plugin) ***$ pytest -m slow --slow examples/test_slow.py
examples/test_slow.py .                                                                                           [100%]
```