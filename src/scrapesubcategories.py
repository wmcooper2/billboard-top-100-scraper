"""Stage 2. Module for Billboard Top 100 scraping."""
#stand lib
from pprint import pprint
from time import sleep

#3rd party
from bs4 import SoupStrainer
from pathlib import Path

#custom
from constants import *
from scrapeutil import *

def format_regex_string(year):
    """Formats the search string for the regex. Returns String."""
    return "\/archive\/charts\/"+year+"\/"

def scrape():
    """Scrape the subcategories from www.billboard.com. Returns None."""
    print("--- SCRAPE SUBCATEGORIES, STARTED ---")
    todo, finished = scrape_setup(YEARFIN, SUBCATEGORYERROR, SUBCATEGORYFIN)
    fin_len     = len(finished)
    todo_len    = len(todo)
    print("finished:", fin_len)
    print("todo    :", todo_len)

    allurls = []
    for link in sorted(todo):
        try:
            soup = get_soup(link, filter_=A_TAGS)
            year = get_year(link)
            pattern = format_regex_string(year)
            a_tags = get_links(soup, pattern) 
            hrefs = get_hrefs(a_tags)
            allurls += list(map(lambda x: HOMEPAGE+x, hrefs))
            print("Done:", link)
        except:
            print("Error:", link)
            save_append_line(link, SUBCATEGORYERROR)
    save(allurls, SUBCATEGORYFIN)
    print("--- SCRAPE SUBCATEGORIES, FINISHED ---")

if __name__ == "__main__":
    scrape()
