#!/usr/bin/env python3.7
# billboardgui.py
"""Stage 2. Module for Billboard Top 100 scraping."""

# stand lib
from pprint import pprint
from time import sleep
from typing import Text

# 3rd party
from bs4 import SoupStrainer
from pathlib import Path

# custom
from constants import A_TAGS
from constants import SUB_CATEGORY_ERR
from constants import SUB_CATEGORY_FIN
from constants import YEAR_FIN
from constants import HOME_PAGE
from scrapeutil import get_hrefs
from scrapeutil import get_links
from scrapeutil import get_soup
from scrapeutil import get_year
from scrapeutil import format_regex_string
from scrapeutil import load_file_list
from scrapeutil import save
from scrapeutil import save_append_line
from scrapeutil import scrape_setup


def scrape() -> None:
    """Scrape the subcategories from www.billboard.com. Returns None."""
    print("--- SCRAPE SUBCATEGORIES, STARTED ---")
    todo, finished = scrape_setup(YEAR_FIN, SUB_CATEGORY_FIN)
    fin_len = len(finished)
    todo_len = len(todo)
    print("finished:", fin_len)
    print("todo    :", todo_len)

    errors = load_file_list(SUB_CATEGORY_ERR)
    allurls = []
    for link in todo:
        try:
            soup = get_soup(link, filter_=A_TAGS)
            year = get_year(link)
            pattern = format_regex_string(year)
            a_tags = get_links(soup, pattern) 
            hrefs = get_hrefs(a_tags)
            allurls += list(map(lambda x: HOME_PAGE+x, hrefs))
            print("Done:", link)
        except:
            print("Error:", link)
            errors.append(link)
            save_append_line(link, SUB_CATEGORY_ERR)
    save(allurls, SUB_CATEGORY_FIN)
    save(list(set(errors)), SUB_CATEGORY_ERR)
    print("--- SCRAPE SUBCATEGORIES, FINISHED ---")
    return None

if __name__ == "__main__":
    scrape()
