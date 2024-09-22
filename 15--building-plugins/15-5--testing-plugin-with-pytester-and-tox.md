## Testing the plugin with pytester and tox

See `15--building-plugins/installable-plugin-with-pytester-and-tox/tox.ini`.

See also:

- Tox: Generative environment list

https://tox.wiki/en/4.20.0/user_guide.html#generative-environment-list

There is no need to install the pytest plugin in the virtual environment.
Tox will install the plugin in each test environment.
```unix
$ source venv_plugin/bin/activate
$ pip install tox
$ pip uninstall pytest_skip_slow_by_ax_va
$ cd 15--building-plugins/installable-plugin-with-pytester-and-tox
```

Replace `<my_email>` in `pyproject.toml` with a correct email.
Run tox in parallel with `--parallel` and reduce the tox output with `-q`.
```unix
$ tox -q --parallel
***
  py311-pytest70: OK (2.74 seconds)
  py311-pytest80: OK (2.59 seconds)
  py311-pytest82: OK (2.82 seconds)
  py311-pytest83: OK (2.72 seconds)
  py312-pytest70: OK (2.80 seconds)
  py312-pytest80: OK (2.79 seconds)
  py312-pytest82: OK (2.77 seconds)
  py312-pytest83: OK (2.73 seconds)
  congratulations :) (2.90 seconds)
```