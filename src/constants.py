#!/usr/bin/env python3
"""Constants for scraping www.billboard.com"""

#stand lib
from pathlib import Path

#3rd party
from bs4 import SoupStrainer


CWD             = str(Path().cwd())
HOME            = "https://www.billboard.com"
A_TAGS          = SoupStrainer("a")
DIVS            = SoupStrainer("div")
YEARS           = CWD+"/../data/years.txt"
YEARLINKS       = CWD+"/../data/yearlinks.txt"
SUBCATEGORYLINKS= CWD+"/../data/subcategories.txt"
ISSUELINKS      = CWD+"/../data/issuelinks.txt"
RANKINGS_DIR    = CWD+"/../rankings/"
ERRORS          = CWD+"/../errors.txt"
ERRORS_NEW      = CWD+"/../errors_new.txt"
