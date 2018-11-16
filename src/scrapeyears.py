#!/usr/bin/env python3
"""Scrapes the year-links from the main page."""

#3rd party
from bs4 import SoupStrainer

#custom
import scrapingtools as tools

if __name__ == "__main__":
    a_tags = SoupStrainer("a")
    HOME = "https://www.billboard.com/archive/charts"
    soup = tools.get_soup(HOME, filter_=a_tags)
    links = tools.get_links(soup, "\/archive\/charts\/[0-9]*")
    tools.save_list(links, "../data/years.txt")
