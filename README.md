<!--
MIT License

Copyright (c) 2023 Dishant B. (@dishb) <code.dishb@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
-->

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
There are 2 options for how you can use `monstera`.

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
    | `git clone https://github.com/dishb/monstera.git` |

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

## Code of Conduct
This project is goverened by the Contributor Covenant Code of Conduct.
We ask that you read the full Code of Conduct in the [`./CODE_OF_CONDUCT.md`](https://github.com/dishb/monstera/blob/main/CODE_OF_CONDUCT.md) file.

## License:
This project is licensed under the `MIT License`. The full copyright can be found in the [`./LICENSE.md`](https://github.com/dishb/monstera/blob/main/LICENSE.md) file.
