#!/usr/bin/env python3.7
# billboardgui.py
"""Scrapes the issue dates' links."""

# stand lib
from pathlib import Path
from pprint import pprint

# custom
from constants import HOME_PAGE
from constants import ISSUE_ERR
from constants import ISSUE_FIN
from constants import SUB_CATEGORY_FIN
from scrapeutil import get_hrefs
from scrapeutil import get_links
from scrapeutil import get_soup
from scrapeutil import load_file_list
from scrapeutil import save
from scrapeutil import save_append
from scrapeutil import scrape_setup


def format_search_string(str1, str2):
    """Formats the search string for the regex. Returns String."""
    return "/{0}/{1}/".format(str(str1), str(str2))


def scrape():
    """Scrapes links from issue-date pages from www.billboard.com. 
        Returns None."""
    print("--- ISSUE DATE SCRAPING, STARTED --- ")
    todo, finished = scrape_setup(SUB_CATEGORY_FIN, ISSUE_FIN)
    fin_len = len(finished)
    todo_len = len(todo)
    print("finished:", fin_len)
    print("todo    :", todo_len)

    errors = load_file_list(ISSUE_ERR)
    for link in sorted(todo):
        try:
            soup = get_soup(link, filter_=A_TAGS)

            #rearrange url suffix
            charts = Path(link).parts[-3]
            subcat = Path(link).parts[-1]

            pattern = format_search_string(charts, subcat)
            issuedates = get_links(soup, pattern)
            hrefs = get_hrefs(issuedates)
            links = sorted(list(map(lambda x: HOME_PAGE + x, hrefs)))
            save_append(links, ISSUE_FIN)
            print("Saved :: ", link)
        except AttributeError:
            errors.append(link)
        except KeyboardInterrupt:
            print("Stopped manually.")
    save(errors, list(set(ISSUE_ERR)))
    print("--- ISSUE DATE SCRAPING, FINISHED --- ")


if __name__ == "__main__":
    scrape()
