#!/usr/bin/env python3.7
# billboardgui.py
"""Scrapes the year-links from the main page."""

# custom
from constants import (
    A_TAGS,
    HOME_PAGE,
    YEAR_FIN,
    YEAR_PAGE)
from scrapeutil import (
    get_soup,
    get_links,
    get_hrefs,
    save)


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
