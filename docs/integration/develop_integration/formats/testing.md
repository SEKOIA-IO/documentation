# Test your Python parser 

## Test files

To validate the parser of a format, a set of test files should be hosted in the directory `tests` of the format.

A test file is a [JSON](https://json.org) document, containing an input (`input`) and an expectation (`expected`).

The input hosts two information:

- the identifier of the format the test should verify (defined in the field `sekoiaio.intake.dialect_uuid`)
- the raw event (defined in the field `message`)

The expectation contains the [structured event](structured_event.md) expected as the output of the parser for the raw event.

## Create a new test

In order to create a new test, you can use the script `utils/create_test.py` to generate a new test file.

The script accept the following arguments:

- The path to the test file to create. Supply the path to the test file in the format directory.
- The raw event: You can provide the raw event as an argument of the script, or through the stdin with the argument `-`

By suppling the path of the test file in the format directory, the script will read manifest information of the format.

```shell
$ cd utils
$ poetry install  # optional, only when dependencies are not already installed
$ poetry run python3 create_test.py ../My\ module/my-format/tests/test1.json "My raw event"
$ cat /tmp/raw_event.txt | poetry run python3 create_test.py ../My\ module/my-format/tests/test2.json -
```

## Validate parser

To execute the test against the parser, go to the `utils` directory, then execute pytest with `test_formats.py` as argument:

```shell
$ cd utils
$ poetry install  # optional, only when dependencies are not already installed
$ poetry run pytest test_formats.py -vv
```

All parsers will be verified against the tests associated to their format.

To execute a subset of test, you could define some options:

- `poetry run pytest test_formats.py --changes`: to only run tests for updated parsers
- `poetry run pytest test_formats.py --module='module-name'`: to only run tests for a specific module (`module-name` correspond to the name defined in the manifest of the module)
- `poetry run pytest test_formats.py --format='format-name'`: to only run tests for a specific format (`format-name` correspond to the name defined in the manifest of the format)