#!/usr/bin/env python3.7
# billboardgui.py
"""Constants for Billboard Top 100 scraping program."""

# stand lib
from pathlib import Path

# 3rd party
from bs4 import SoupStrainer

SLEEP_TIME = 1

# Program dirs/files
CWD = str(Path().cwd())
A_TAGS = SoupStrainer("a")
DIVS = SoupStrainer("div")
DATA_DIR = CWD+"/../data/"
RANKING_DIR = CWD+"/../rankings/"

ISSUE_ERR = DATA_DIR+"issueerror.txt"
ISSUE_FIN = DATA_DIR+"issuefin.txt"
RANK_ERR = DATA_DIR+"rankerror.txt"
RANK_FIN = DATA_DIR+"rankfin.txt"
SUB_CATEGORY_ERR = DATA_DIR+"subcategoryerror.txt"
SUB_CATEGORY_FIN = DATA_DIR+"subcategoryfin.txt"
YEAR_ERR = DATA_DIR+"yearerror.txt"
YEAR_FIN = DATA_DIR+"yearfin.txt"

# urls
HOME_PAGE = "https://www.billboard.com"
YEAR_PAGE = HOME_PAGE+"/archive/charts"

DIRS = [
    DATA_DIR,
    RANKING_DIR,
]

FILES = [
    ISSUE_ERR,
    ISSUE_FIN,
    RANK_ERR,
    RANK_FIN,
    SUB_CATEGORY_ERR,
    SUB_CATEGORY_FIN,
    YEAR_ERR,
    YEAR_FIN,
]
