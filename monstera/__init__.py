"""
monstera

Author: Dishant B. (@dishb) code.dishb@gmail.com
License: MIT License
Source: https://github.com/dishb/monstera
"""

import sys
import platform
from os.path import dirname
from subprocess import run as sp_run
from typing import Dict, List, Union

import distro

__source__ = "https://github.com/dishb/monstera"
__license__ = "MIT License"
__version__ = "0.0.1"
__author__ = "Dishant B. (@dishb) <code.dishb@gmail.com>"
__copyright__ = """
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
                """

def run(packages: Union[List[str], str] = None) -> Dict[str, str]:
    """
    monstera's main function. Gets the following information about the user's machine:
    Meant for programming use. Do not use monstera._main().

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

    Args:
        packages (List[str] | str, optional): A list of packages (or one singular package) that you
        want information on. Defaults to None.

    Returns:
        Dict[str, str]: The information as a Python dictionary. This includes information on the
        packages.
    """

    if platform.system() == "Darwin" or platform.system() == "Linux":
        pip_cmd = "pip3"
    else:
        pip_cmd = "pip"

    pkg_vers = []
    pkg_locs = []

    if packages is not None:
        for pkg in packages:
            output1 = sp_run([pip_cmd, "show", pkg], check = True, capture_output = True).stdout
            output1 = output1.decode().split("\n")

            pkg_locs.append(output1[7].split()[1])
            pkg_vers.append(output1[1].split()[1])

    major = sys.version_info[0]
    minor = sys.version_info[1]
    patch = sys.version_info[2]
    level = sys.version_info[3]
    if level == "candidate":
        level = "release candidate"
    else:
        level += " release"

    oper_sys = platform.system() # pylint: disable = invalid-name
    if oper_sys == "":
        oper_sys = "Could not be determined." # pylint: disable = invalid-name
        os_version = "Could not be determined."
        arch = "Could not be determined."

    if oper_sys.lower() == "darwin":
        oper_sys = "macOS" # pylint: disable = invalid-name
        os_version = platform.mac_ver()[0]
        arch = platform.architecture()[0]
    elif oper_sys.lower() == "windows":
        os_version = platform.win32_ver()[0]
        arch = platform.architecture()[0]
    elif oper_sys.lower() == "linux":
        oper_sys = distro.name() # pylint: disable = invalid-name
        os_version = distro.version(best = True)
        arch = platform.architecture()[0]

    python_loc = dirname(sys.executable)

    output2 = sp_run([pip_cmd, "-V"], check = True, capture_output = True).stdout
    output2 = output2.split()

    pip_ver = output2[1].decode()
    pip_loc = dirname(output2[3].decode())

    info = {"python_version": f"{major}.{minor}.{patch}",
            "python_location": python_loc,
            "release_level": level,
            "os": oper_sys,
            "os_version": os_version,
            "architecture": arch,
            "pip_version": pip_ver,
            "pip_location": pip_loc
            }

    if packages is not None:
        for index, pkg in enumerate(packages):
            info[f"{pkg}_version"] = pkg_vers[index]
            info[f"{pkg}_location"] = pkg_locs[index]

    return info
