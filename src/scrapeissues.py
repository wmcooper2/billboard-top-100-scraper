"""Scrapes the issue dates' links."""
#stand lib
from pathlib import Path

#custom
from constants import *
from scrapeutil import *

def format_search_string(str1, str2):
    """Formats the search string for the regex. Returns String."""
    return "/{0}/{1}/".format(str(str1), str(str2))

def scrape():
    """Scrapes links from issue-date pages from www.billboard.com. 
        Returns None."""
    print("--- ISSUE DATE SCRAPING, STARTED --- ")
    todo, finished = scrape_setup(SUBCATEGORYFIN, ISSUEERROR, ISSUEFIN)
    fin_len     = len(finished)
    todo_len    = len(todo)
    print("finished:", fin_len)
    print("todo    :", todo_len)

    for link in sorted(todo):
        try:
            soup = get_soup(link, filter_=A_TAGS)

            #rearrange url suffix
            charts = Path(link).parts[-3]
            subcat = Path(link).parts[-1]

            pattern = format_search_string(charts, subcat)
            issuedates = get_links(soup, pattern)
            hrefs = get_hrefs(issuedates)
            links = sorted(list(map(lambda x: HOMEPAGE+x, hrefs)))
            save_append(links, ISSUEFIN)
            print("Saved :: ", link)
        except:
            print("Error:", link)
            save_append_line(link, ISSUEERROR)
    print("--- ISSUE DATE SCRAPING, FINISHED --- ")

if __name__ == "__main__":
    scrape()
