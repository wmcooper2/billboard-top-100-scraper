#!/usr/bin/env python3.7
# billboardgui.py
"""Setup the files and dirs for Billboard Top 100 scraping program."""

# stand lib
from pathlib import Path
from typing import Text

# custom
from constants import DIRS
from constants import FILES


def make_dirs() -> None:
    """Makes the dirs needed for the program. Returns None."""
    for d in DIRS:
        path = Path(d)
        if not check(path):
            path.mkdir()
            print("Created:", str(path))
        else:
            print("Exists:", str(path))
    return None
            
def make_files() -> None:
    """Makes the files needed for the program. Returns None."""
    for f in FILES:
        path = Path(f)
        if not check(path):
            path.touch()
            print("Created:", str(path))
        else:
            print("Exists:", str(path))
    return None

def check(string: Text) -> bool:
    """Checks for file/dir existence. Returns Boolean."""
    return Path(string).exists()
