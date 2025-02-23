# Coverage

## Generating HTML reports

### With running a coverage run
```unix
$ pytest --cov=cards --cov-report=html 07--test-strategies
***
Coverage HTML written to dir htmlcov
```
Open `htmlcov/index.html`.

<p align="center">
  <img src="https://github.com/ax-va/Pytest-Okken-2022/blob/main/09--coverage/09-2--generating-html-reports.png" width="700"/>
</p>

### After running a previous coverage run
```unix
$ pytest --cov=cards 07--test-strategies
$ coverage html
```