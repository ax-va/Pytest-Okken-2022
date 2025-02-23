# Debugging test failures

## The full list of pdb commands

- https://docs.python.org/3/library/pdb.html#debugger-commands

## pdb meta commands

### `h(elp)`

- to print a list of commands.

### `h(elp) <command>`

- to print help on `<command>`.

### `q(uit)`

- to exits pdb.

## pdb commands to see where you are

### `l(ist)`

- to list 11 lines around the current line; using it again lists the next 11 lines, and so on.

### `l(ist) .`

- to list 11 lines around the current line.

### `l(ist) <first>, <last>`

- to list a specific set of lines.

### `ll`

- to list all source code for the current function.

### `w(here)`

- to print the stacktrace.

## pdb commands to look at values

### `p(rint) <expr>`

- to evaluate `<expr>` and print the value.

### `pp <expr>`

- to evaluate `<expr>` and print the value using pretty-print from the pprint module.

### `a(rgs)`

- to print the argument list of the current function.

## pdb commands to execute code lines

### `s(tep)`

- to execute the current line and go to the next line, also into a function.

### `n(ext)`

- to execute the current line and go to the next line in the current function .

### `r(eturn)`

- to continue and go to the last line of the function.

### `c(ontinue)`

- to continue until the next breakpoint; with `--trace` to continue until the start of the next test.

### `unt(il) <lineno>`

- to continue until the given line number.