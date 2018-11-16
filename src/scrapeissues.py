#!/usr/bin/env python3
"""Scrapes the issue dates' links."""

#stand lib
from pathlib import Path
from pathlib import PurePath
from pprint import pprint

#custom
from constants import *
import scrapingtools as tools


if __name__ == "__main__":
    print("SCRAPING ISSUE DATES...")
    links = tools.load_list(SUBCATEGORYLINKS)
    for link in links:
        soup = tools.get_soup(link, filter_=A_TAGS)

        #rearrange url suffix
        charts = Path(link).parts[-3]
        subcat = Path(link).parts[-1]
        search_string = "/{0}/{1}/".format(charts, subcat)

        issuedates = tools.get_links(soup, search_string)
        issuelinks = map(tools.get_href, issuedates)
        fullpaths = map(tools.add_base_url, issuelinks)

        tools.save_link_list(fullpaths, ISSUELINKS)
        print("SCRAPED :: ", link)

    print("FINISHED SCRAPING ISSUE DATES")
