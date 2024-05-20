# Determining the test Scope

Security? Performance? Loading? Input validation?

# Considering the software architecture

Investigate the software architecture to use this knowledge for testing

# Prioritizing features for testing

## Prioritize features for testing

- *Recent*: New functionality that has been recently repaired, refactored, or modified.
- *Core*: The essential functions that must continue to work in order for the product to be useful.
- *Risk*: Areas of the application that pose more risk, such as areas important to customers but not used regularly by the development team or parts that use third-party code you don't quite trust.
- *Problematic*: Functionality that frequently breaks or often gets defect reports against it.
- *Expertise*: Features or algorithms understood by a limited subset of people.

## Examples of testing `Cards`

- Test core features thoroughly.
- Test non-core features with at least one test case.
- Test the CLI in isolation.

# Creating test cases

## Create test cases

1. Start with a **non-trivial**, happy-path test case.

2. Then look at test cases that represent
   - interesting sets of input,
   - interesting starting states,
   - interesting end states, or
   - all possible error states.

## Examples of testing `count` of `Cards`

- For a database with three elements, `count` returns 3.

Then

- `count` from an empty database
- `count` with one item
- `count` with more than one item (can be duplicated with 1 and omitted)

## Examples of test cases for `add` of `Cards`

- `add` to an empty database, with summary
- `add` to a non-empty database, with summary
- `add` a card with both summary and owner set
- `add` a card with a missing summary
- `add` a duplicate card

## Examples of test cases for `delete` of `Cards`

- `delete` one from a database with more than one
- `delete` the last card
- `delete` a non-existent card

## Examples of test cases for `start` and `finish` of `Cards` that are considered together

- `start` from "todo", "in prog", and "done" states
- `start` an invalid ID
- `finish` from "todo", "in prog", and "done" states
- `finish` an invalid ID

## Remaining test case examples

- `update` the owner of a card
- `update` the summary of a card
- `update` owner and summary of a card at the same time
- `update` a non-existent card
- `list` from an empty database
- `list` from a non-empty database
- `config` returns the correct database path
- `version` returns the correct version

# Writing a test strategy

Write a test strategy and share it with your team. 
Include the initial test case list.
