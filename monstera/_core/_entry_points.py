from argparse import ArgumentParser
from os import getcwd
from os.path import exists
from pathlib import Path

from colorama import Fore, Style, init, deinit

from ._main import run

def _console() -> int:
    """
    monstera's main entry point. Not meant for programming use. Instead, use monstera.run().
    Prints the information that monstera.run() returns.

    Returns:
        int: The exit code.
    """

    description = """description: A cross-platform CLI to quickly retrieve
system information to make issue management easier."""

    init(autoreset = True)

    parser = ArgumentParser(prog = "monstera",
                            description = description,
                            )
    parser.add_argument("-m", "--module",
                        nargs = "*",
                        action = "store",
                        help = """find information on one or more Python packages. includes version
                                  and location.""",
                        required = False,
                        dest = "names",
                        metavar = "MODULE NAMES"
                        )
    parser.add_argument("-v", "--version",
                        action = "store_true",
                        help = "print the version of monstera.",
                        required = False,
                        dest = "version"
                        )
    parser.add_argument("-c", "--copyright",
                        action = "store_true",
                        help = "print the license/full copyright of monstera.",
                        required = False,
                        dest = "license"
                        )

    args = parser.parse_args()

    if args.version:
        print("monstera: v0.0.5")

        return 0

    if args.license:
        print("""
monstera is licensed under the MIT License:

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
SOFTWARE
"""
             )

        return 0

    packages = args.names
    
    if packages is None:
        cwd = Path(getcwd())
        if exists(cwd / "requirements.txt"):
            with open(cwd / "requirements.txt") as file:
                lines = file.read()
                lines = lines.split("\n")
                file.close()

        packages = lines
    
    info = run(packages)

    print(Fore.YELLOW + Style.BRIGHT + "\nPython:"
          + Style.RESET_ALL
          + f" {info['python_version']}, {info['release_level']}"
          )

    print(Fore.YELLOW + Style.BRIGHT + "\nPython Location:"
          + Style.RESET_ALL
          + f" {info['python_location']}"
          )

    print(Fore.YELLOW + Style.BRIGHT + "\nOperating System:"
          + Style.RESET_ALL
          + f" {info['os']} {info['os_version']}"
          )

    print(Fore.YELLOW + Style.BRIGHT + "\nArchitecture:" +
          Style.RESET_ALL
          + f" {info['architecture']}"
          )

    print(Fore.YELLOW + Style.BRIGHT + "\nPip:"
          + Style.RESET_ALL
          + f" {info['pip_version']}"
          )

    print(Fore.YELLOW + Style.BRIGHT + "\nPip Location:"
          + Style.RESET_ALL
          + f" {info['pip_location']}"
          )

    if packages is not None:
        for pkg in packages:
            if info[f"{pkg}_version"] == f"{pkg} is not installed.":
                print(Fore.RED + Style.BRIGHT + "\nError:"
                      + Style.RESET_ALL
                      + f" {pkg} is not installed."
                      )
            else:
                print(Style.BRIGHT + Fore.BLUE + f"\n{pkg}:")
                print(f"    Location: {info[f'{pkg}_location']}")
                print(f"    Version: {info[f'{pkg}_version']}")

    print("")

    deinit()
    return 0
