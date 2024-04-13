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

from pytest import main

def test_empty_flag() -> None:
    """
    Tests the command: monstera -m

    Only meant to be run by Dishant B. in his environment.
    """

    command = run(["monstera", "-m"],
                  check = False,
                  capture_output = True
                  )
    return_code = command.returncode
    output = command.stdout.decode()

    expected_output = """
Python: 3.12.2, final release

Python Location: /Library/Frameworks/Python.framework/Versions/3.12/bin

Operating System: macOS 14.3.1

Architecture: 64bit

Pip: 24.0

Pip Location: /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages

"""

    assert return_code == 0
    assert output == expected_output

def test_no_package() -> None:
    """
    Tests the command: monstera

    Only meant to be run by Dishant B. in his environment.
    """

    command = run(["monstera"],
                  check = False,
                  capture_output = True
                  )
    return_code = command.returncode
    output = command.stdout.decode()

    expected_output = """
Python: 3.12.2, final release

Python Location: /Library/Frameworks/Python.framework/Versions/3.12/bin

Operating System: macOS 14.3.1

Architecture: 64bit

Pip: 24.0

Pip Location: /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages

"""

    assert return_code == 0
    assert output == expected_output

def test_single_package() -> None:
    """
    Tests the command: monstera -m monstera

    Only meant to be run by Dishant B. in his environment.
    """

    command = run(["monstera", "-m", "monstera"],
                  check = False,
                  capture_output = True
                  )
    return_code = command.returncode
    output = command.stdout.decode()

    expected_output = """
Python: 3.12.2, final release

Python Location: /Library/Frameworks/Python.framework/Versions/3.12/bin

Operating System: macOS 14.3.1

Architecture: 64bit

Pip: 24.0

Pip Location: /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages

monstera:
    Location: /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages
    Version: 0.0.5

"""

    assert return_code == 0
    assert output == expected_output

def test_multiple_packages() -> None:
    """
    Tests the command: monstera -m monstera pytest

    Only meant to be run by Dishant B. in his environment.
    """

    command = run(["monstera", "-m", "monstera", "pytest"],
                  check = False,
                  capture_output = True
                  )
    return_code = command.returncode
    output = command.stdout.decode()

    expected_output = """
Python: 3.12.2, final release

Python Location: /Library/Frameworks/Python.framework/Versions/3.12/bin

Operating System: macOS 14.3.1

Architecture: 64bit

Pip: 24.0

Pip Location: /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages

monstera:
    Location: /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages
    Version: 0.0.5

pytest:
    Location: /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages
    Version: 8.0.2
"""

    assert return_code == 0
    assert output == expected_output

if __name__ == "__main__":
    main()
