#!/usr/bin/env python3
"""Scrapes the subcategories. These subcategories are how the year-categories are divided."""

#custom
from constants import *
import scrapingtools as tools

if __name__ == "__main__":
    all_years           = []

    # load urls from /data/years.txt
    with open(YEARS, "r") as years:
        for line in years.readlines():
            all_years.append(line.strip())

    # append each url to HOME
    all_links = map(tools.add_base_url, all_years)
    tools.save_link_list(all_links, YEARLINKS)   



