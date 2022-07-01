# montyhallsim

[![PyPI Version](https://img.shields.io/pypi/v/montyhallsim.svg?style=flat)](https://pypi.org/project/montyhallsim/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/montyhallsim.svg?style=flat)](https://pypi.org/project/montyhallsim/) [![License](https://img.shields.io/pypi/l/montyhallsim.svg?style=flat)](LICENSE)

A command-line interface for simulating the [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem).

## Installation

**PyPI**

```bash
$ pip install montyhallsim
```

**GitHub**

```bash
$ git clone https://github.com/mrwolferinc/montyhallsim.git
$ cd montyhallsim
$ python setup.py install
```

## Usage/Examples

The simplest usage of the interface:

```bash
$ montyhallsim
```

To run a simulation without swapping doors:

```bash
$ montyhallsim -n
```

To run a simulation with a specified number of rounds played:

```bash
$ montyhallsim -r 15
```

### Arguments

Syntax: `montyhallsim [-r [ROUNDS]] [-n]`

| Argument                       | Type     | Description                                             |
| ------------------------------ | -------- | ------------------------------------------------------- |
| -r [ROUNDS], --rounds [ROUNDS] | optional | Set the number of rounds to be played - defaults to 10. |
| -n, --no-swap                  | optional | Run a simulation without swapping doors.                |

> **Note:** If you are running this package locally, then you will need to call `python -m montyhallsim` instead of `montyhallsim`.

## Running Tests

Tests are located inside the `tests` directory and are run using [pytest](https://github.com/pytest-dev/pytest). To run tests, run the following commands:

```bash
$ pip install pytest
$ pip install -e .
$ pytest
```

## Contributing

Contributions are always welcome!

See [CONTRIBUTING.md](.github/CONTRIBUTING.md) for ways to get started.

Please adhere to this project's [code of conduct](.github/CODE_OF_CONDUCT.md) while contributing.

## License

[MIT](https://opensource.org/licenses/MIT)
