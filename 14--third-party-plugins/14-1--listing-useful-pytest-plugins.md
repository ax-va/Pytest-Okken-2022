# Listing useful pytest plugins

## Plugins to change the normal test run flow

Pytest will run each file in alphabetical order in a single directory. 
Each test is run in the order it appears in a file.

- **pytest-order** to specify the order using a marker.

- **pytest-randomly** to randomize the order, first by file, then by class, then by test.

- **pytest-repeat** to repeat a single test or multiple tests a specific number of times.

- **pytest-rerunfailures** to re-run failed tests that is helpful for flaky tests.

- **pytest-xdist** to run tests in parallel, either using multiple CPUs on one machine or multiple remote machines.

## Plugins to alter or enhance output

Pytest reports tracebacks and output from failed tests after all tests have completed.

- **pytest-instafail** to report tracebacks and output from failed tests right after the failure.

- **pytest-sugar** to show green checkmarks for passing tests (instead of dots), 
to instantly show failures, and to display a progress bar.

- **pytest-html** to generate HTML reports that can be extended with extra data and images, 
such as screenshots of failure cases.

## Plugins for web development

- **pytest-selenium** to provide fixtures for configuration of browser-based tests.

- **pytest-splinter** to use Splinter (built on top of Selenium as a higher level interface) more easily from pytest.

- **pytest-playwright** to write end-to-end tests for web apps with Playwright and pytest.

- **pytest-django** and **pytest-flask** to make testing Django and Flask applications easier with pytest.

## Plugins for fake data

- **Faker** to generate fake data with; with pytest by using Faker fixture.

- **model-bakery** to generate Django model objects with fake data.

- **pytest-factoryboy** to use fixtures for Factory Boy, a database model data generator.

- **pytest-mimesis** to generates fake data similar to Faker, but Mimesis is quite a bit faster.

## Plugins to extend pytest functionality

- **pytest-cov** to runs coverage while testing.

- **pytest-benchmark** to runs benchmark timing on code within tests.

- **pytest-timeout** to run tests not too long.

- **pytest-asyncio** to test async functions.

- **pytest-bdd** to write behavior-driven development (BDD)–style tests with pytest.

- **pytest-freezegun** to freeze time so that any code that reads the time will get the same value during a test;
a particular date or time can be set.

- **pytest-mock** to wrap the unittest.mock patching API.