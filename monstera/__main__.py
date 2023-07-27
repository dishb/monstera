"""
monstera

Author: Dishant B. (@dishb) code.dishb@gmail.com
License: MIT License
Source: https://github.com/dishb/monstera
"""

from sys import exit as sys_exit
from argparse import ArgumentParser

from colorama import Fore, Style, init, deinit

from .__init__ import run

def _main() -> int:
    """
    monstera's main entry point. Gets the following information about the user's machine:
    Not meant for programming usage. Please use monstera.run().

    - Operating system
    - OS version
    - Machine architecture
    - Version of Python
    - Python's location
    - Version of pip
    - pip's location

    and optionally:

    - Version of a package
    - The package's location

    Note that versions and locations of Python, pip, and packages are dependent on the environment
    they are run in.

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

    args = parser.parse_args()

    packages = args.names
    info = run(packages = packages)

    print(Fore.YELLOW + Style.BRIGHT + "\nPython:"
          + Style.RESET_ALL
          + f" {info['python_version']}, {info['release_level']}"
          )

    print(Fore.RED + Style.BRIGHT + "\nPython Location:"
          + Style.RESET_ALL
          + f" {info['python_location']}"
          )

    print(Fore.GREEN + Style.BRIGHT + "\nOperating System:"
          + Style.RESET_ALL
          + f" {info['os']} {info['os_version']}"
          )

    print(Fore.BLUE + Style.BRIGHT + "\nArchitecture:" +
          Style.RESET_ALL
          + f" {info['architecture']}"
          )

    print(Fore.MAGENTA + Style.BRIGHT + "\nPip:"
          + Style.RESET_ALL
          + f" {info['pip_version']}"
          )

    print(Fore.CYAN + Style.BRIGHT + "\nPip Location:"
          + Style.RESET_ALL
          + f" {info['pip_location']}"
          )

    if packages is not None:
        for pkg in packages:
            print(Style.BRIGHT + f"\n{pkg}:")
            print(f"    Location: {info[f'{pkg}_location']}")
            print(f"    Version: {info[f'{pkg}_version']}")

    print("")

    deinit()
    return 0

if __name__ == "__main__":
    sys_exit(_main())
