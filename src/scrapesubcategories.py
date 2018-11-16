#!/usr/bin/env python3
"""Scrapes subcategories for more links."""

#stand lib
from pprint import pprint

#3rd party
from bs4 import SoupStrainer
from pathlib import Path

#custom
import scrapingtools as tools
from constants import *

if __name__ == "__main__":
    a_tags              = SoupStrainer("a")
    urls                = []

    print("SCRAPING SUBCATEGORIES...")
    with open(YEARLINKS, "r") as years:
        for line in years.readlines():
            urls.append(line.strip())
    for url in urls:
        soup = tools.get_soup(url, filter_=a_tags)
        year = Path(url).parts[-1]
        search_string = "\/archive\/charts\/"+str(year)+"\/"
        links = tools.get_links(soup, search_string) 
        temp = []
        for link in links:
            temp.append(link.get("href").strip())         

        full_links = map(tools.add_base_url, temp)
        tools.save_link_list(full_links, SUBCATEGORYLINKS)
        print("FINISHED ::", url)
    print("SCRAPING SUBCATEGORIES COMPLETE")
