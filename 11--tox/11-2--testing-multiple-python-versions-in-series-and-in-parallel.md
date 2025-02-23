# Tox

## Run tox in a series
```unix
$ cd cards_proj_tox
$ tox -c tox_multiple_pythons.ini
***
  py310: OK (9.23=setup[7.75]+cmd[1.49] seconds)
  py311: OK (2.67=setup[1.66]+cmd[1.01] seconds)
  py312: OK (9.43=setup[7.93]+cmd[1.50] seconds)
  congratulations :) (21.41 seconds)
 $ cd ..
```

## Run tox in parallel
```unix
$ cd cards_proj_tox
$ tox -c tox_multiple_pythons.ini -p
***
  py310: OK (3.21=setup[2.01]+cmd[1.21] seconds)
  py311: OK (3.18=setup[2.02]+cmd[1.16] seconds)
  py312: OK (3.30=setup[2.07]+cmd[1.23] seconds)
  congratulations :) (3.37 seconds)
$ cd ..
```