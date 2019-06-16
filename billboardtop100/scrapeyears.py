#!/usr/bin/env python3.7
# billboardgui.py
"""Scrapes the year-links from the main page."""

# custom
from constants import A_TAGS
from constants import HOME_PAGE
from constants import YEAR_FIN
from constants import YEAR_PAGE
from scrapeutil import get_soup
from scrapeutil import get_links
from scrapeutil import get_hrefs
from scrapeutil import save


def scrape() -> None:
    """Scrapes the year-links from www.billboard.com. Returns None."""
    print("--- SCRAPING YEARS, STARTED ---")
    soup = get_soup(YEAR_PAGE, filter_=A_TAGS)
    links = get_links(soup, "\/archive\/charts\/[0-9]*")
    links = get_hrefs(links)
    links = list(map(lambda x: HOME_PAGE + x, links))
    save(links, YEAR_FIN)
    print("--- SCRAPING YEARS, FINISHED ---")
    return None


if __name__ == "__main__":
    scrape()
