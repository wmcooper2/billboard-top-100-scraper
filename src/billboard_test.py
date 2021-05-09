#!/usr/bin/env python3.7
# billboardgui.py
"""Test module for Billboard Top 100 Scraper."""

# 3rd party
import pytest

# custom
from constants import (
    A_TAGS,
    DIRS,
    FILES,
    HOME_PAGE,
    YEAR_FIN,
    YEAR_PAGE)
from filesanddirs import check
from scrapeutil import (
    get_soup,
    get_links,
    get_hrefs,
    save)




#TODO: finish writing tests
def test_dirs_and_files():
    """Ensure the hierarchy for the program is setup."""
    for x in DIRS+FILES:
        assert check(x) is True

def test_year_scraping_href_elements_regex_valid():
    """Ensure that the href structure for scraping the years has not changed."""
    soup = get_soup(YEAR_PAGE, filter_=A_TAGS)
    links = get_links(soup, r"\/archive\/charts\/[0-9]*")
    assert len(links) > 0
    

