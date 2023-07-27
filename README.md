![monstera's banner image](./assets/banner.png)

# monstera

A cross-platform CLI to quickly retrieve system information to make issue management easier.

## Features:
A list of all the information collected:

- Version of Python
- Python's location (where it was installed)
- Python's release type (alpha, beta, candidate, final)
- Version of `pip`
- `pip`'s location (where it was installed)
- Operating system (support for Linux distros)
- OS version
- Version and installation location of packages

A lot of this information depends on the environment that Python is being run in.

## Documentation:
To get more information on how to use `monstera`, you can read the documentation in the [`./docs`](https://github.com/dishb/monstera/tree/main/docs) directory.

## Installation:
`monstera` requires Python 3.9 or higher.

You can install the package with `pip`.

| macOS/Linux | Windows |
| --- | --- |
| `pip3 install monstera` | `pip install monstera` |

## Usage:
There are 2 options for how you can use 'monstera'.

1. Use the CLI:

    | macOS/Linux | Windows |
    | --- | --- |
    | `python3 -m monstera` | `python -m monstera` |

    You can also just call `monstera` directly.

2. Use `monstera` in your code:

    ```python
    import monstera

    monstera.run()
    ```

## Contributing:
To get started with contributing to `monstera`, follow this guide.
It is recommended to read the [`./CONTRIBUTING.md`](https://github.com/dishb/monstera/blob/main/CONTRIBUTING.md) file.

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

## License:
This project is licensed under the `MIT License`. The full copyright can be found in the [`./LICENSE.md`](https://github.com/dishb/monstera/blob/main/LICENSE.md) file.

## Attribution

The background photo in [`./assets/banner.png`](https://github.com/dishb/monstera/blob/main/assets/banner.png) is by [Gilles Lambert](https://unsplash.com/@gilleslambert?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/mSK5nNsAsLY?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

The font used is [Victor Mono](https://github.com/rubjo/victor-mono) (bold).
