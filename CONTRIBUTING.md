# Contributing

This is the documentation for contributing to `monstera`.

## Getting started:

You can get started by following the commands below. 
They'll help you clone the repository and install all the dependencies.

1. Clone the repository:

    | OS Independent |
    | --- |
    | `git clone https://github.com/dishb/monstera` |

    Change to the directory:

    | macOS/Linux | Windows |
    | --- | --- |
    | `cd ./monstera/` | `cd .\monstera\` |

2. Create a virtual environment (optional, but recommended):

    | macOS/Linux | Windows |
    | --- | --- |
    | `python3 -m venv ./.venv/` | `python -m venv .\.venv\` |
    | `source ./.venv/bin/activate` | `.\.venv\Scripts\activate.bat` |

3. Install the dependencies:

    | macOS/Linux | Windows |
    | --- | --- |
    | `pip3 install -r requirements.txt` | `pip install -r requirements.txt` |
    | `pip3 install -r dev-requirements.txt` | `pip install -r dev-requirements.txt` |

4. Install `monstera` in edit mode:

    | macOS/Linux | Windows |
    | --- | --- |
    | `pip3 install -e .` | `pip install -e .` |

## Commits:

When making commits to your clone, we ask that you follow this simple guide.

For the sake of readability, we ask that commit messages be no longer than 50 characters.

Here are titles for each commit. They should prefix the short message and be followed by a colon (:).

An example commit: `title: short message`.

- new feature - feat
- small edit - edit
- a bug/general fix - fix
- a chore (dependecies, code redability) - chore
- initializing commits (adding project files) - init
- documentation related changes - docs

If you have any questions, please ask in the Q&A section of Discussions tab.

## Linting

To make sure our code is maintainable, we use Pylint.
You can lint your code by running the following command in the top level directory of the respository.

| macOS/Linux | Windows |
| --- | --- |
| `pylint $(git ls-files '*.py') --rcfile=./.pylint.rc` | `for /F "delims=" %G in ('git ls-files "*.py"') do pylint "%G" --rcfile=.pylint.rc` |

## Testing

To make sure the code runs without errors or problems, please test your code with Pytest.
Run the following command in the top level directory of the repository.

| macOS/Linux | Windows |
| --- | --- |
| `pytest -q --rootdir=./tests/` | `pytest -q --rootdir=.\tests\` |

