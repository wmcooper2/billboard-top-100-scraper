#!/usr/bin/env python3.7
# billboardgui.py
"""Test module for Billboard Top 100 Scraper."""

# 3rd party
import pytest

# custom
from filesanddirs import *

def test_dirs_and_files():
    for x in dirs+files:
        assert check(x) is True
