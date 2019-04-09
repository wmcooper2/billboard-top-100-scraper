#!/usr/bin/env python3.7
# billboardgui.py
"""Scrape song rankings from www.billboard.com."""

# custom
from constants import DIVS
from constants import ISSUE_FIN
from constants import RANK_FIN
from constants import RANK_ERR
from constants import RANKING_DIR
from scrapeutil import format_file_name
from scrapeutil import get_soup
from scrapeutil import has_data_title
from scrapeutil import load_file_list
from scrapeutil import save_append_line
from scrapeutil import save_ranking
from scrapeutil import scrape_setup


def scrape():
    """Scrapes rankings from www.billboard.com. Returns None."""
    print("--- RANK SCRAPING, STARTED --- ")
    todo, finished = scrape_setup(ISSUE_FIN, RANK_FIN)
    fin_len = len(finished)
    todo_len = len(todo)
    print("finished:", fin_len)
    print("todo    :", todo_len)

    errors = load_file_list(RANK_ERR)
    rank_count = 0
    for link in todo:
        try:
            soup = get_soup(link, filter_=DIVS)
            div_soup = soup.find_all("div")
            for element in div_soup:
                if has_data_title(element):
                    name = format_file_name(link)
                    save_ranking(name, element)
            print("Saved:: ", name)
            save_append_line(link, RANK_FIN)
            rank_count += 1
        except:
            print("Error:", link)
            errors.append(link)
    save(list(set(errors)), RANK_ERR)
    print("rank_count:", str(rank_count))
    print("--- RANK SCRAPING, FINISHED --- ")


if __name__ == "__main__":
    scrape()
