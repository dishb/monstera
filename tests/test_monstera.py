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
Python: 3.12.3, final release

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
Python: 3.12.3, final release

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
Python: 3.12.3, final release

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
Python: 3.12.3, final release

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
