"""Scrapes the year-links from the main page."""
#custom
from constants import *
#import scrapingtools as *
from scrapeutil import *

def scrape():
    """Scrapes the year-links from www.billboard.com. Returns None."""
    print("--- SCRAPING YEARS, STARTED ---")
    a_tags = SoupStrainer("a")
    soup = get_soup(YEARSPAGE, filter_=a_tags)
    links = get_links(soup, "\/archive\/charts\/[0-9]*")
    links = get_hrefs(links)
    links = list(map(lambda x: HOMEPAGE+x, links))
    save(links, "../data/years.txt")
    print("--- SCRAPING YEARS, FINISHED ---")

if __name__ == "__main__":
    scrape()
