from sys import exit as sys_exit

from ._core._entry_points import _console

if __name__ == "__main__":
    sys_exit(_console())
