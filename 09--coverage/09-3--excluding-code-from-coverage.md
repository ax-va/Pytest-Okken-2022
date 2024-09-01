# Excluding code from coverage

## Pragma statement

Exclude either a single line or a code block from testing coverage with a pragma statement
```unix
if __name__ == '__main__':  # pragma: no cover
    main()
```

Notice: beware of coverage-driven development / testing - we don't have to cover 100% of code.