# Generating HTML reports

## With running a coverage run
```unix
$ pytest --cov=cards --cov-report=html 07--test-strategies
###
Coverage HTML written to dir htmlcov
```
Open `htmlcov/index.html`.

## After running a previous coverage run
```unix
$ pytest --cov=cards 07--test-strategies
$ coverage html
```