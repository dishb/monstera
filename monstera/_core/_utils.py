from shutil import which

def _detect_conda() -> bool:
    """
    Detects if the current environment is using conda or pip.

    Returns:
        bool: Whether or not conda is being used.
    """

    if which("conda"):
        return True

    return False
