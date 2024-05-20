# Create test cases
1. Start with a **non-trivial**, "happy path" test case.

2. Then look at test cases that represent
   - interesting sets of input,
   - interesting starting states,
   - interesting end states, or
   - all possible error states.

# Examples of testing `count` of `Cards` 
- For a database with three elements, `count` returns 3.

Then

- `count` from an empty database
- `count` with one item
- `count` with more than one item (can be duplicated with 1 and omitted)

# Examples of testing `add` of `Cards` 
- `add` to an empty database, with summary
- `add` to a non-empty database, with summary
- `add` a card with both summary and owner set
- `add` a card with a missing summary
- `add` a duplicate card

# Examples of testing `delete` of `Cards` 
- `delete` one from a database with more than one
- `delete` the last card
- `delete` a non-existent card