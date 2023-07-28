#
# MIT License
#
# Copyright (c) 2023 Dishant B. (@dishb) <code.dishb@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

"""
monstera

Author: Dishant B. (@dishb) code.dishb@gmail.com
License: MIT License
Source: https://github.com/dishb/monstera
"""

from subprocess import run
from platform import system
from os.path import dirname
from os import chdir

if __name__ == "__main__":
    cwd = dirname(__file__).removesuffix("/utils")
    chdir(cwd)

    if system() == "Darwin" or system() == "Linux":
        PIP_CMD = "pip3"
    else:
        PIP_CMD = "pip"

    run([PIP_CMD, "uninstall", "-y", "monstera"], check = True)

    if system() == "Darwin" or system() == "Linux":
        run(["rm", "-rf", "./monstera.egg-info"], check = True)
    else:
        run(["rmdir", r".\monstera.egg-info"], check = True)
