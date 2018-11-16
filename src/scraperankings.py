#!/usr/bin/env python3
"""Scrape the song rankings. This is the final step to get the data I want."""

#stand lib
from pprint import pprint
from pathlib import Path
from time import sleep

#3rd party
from bs4 import BeautifulSoup

#custom
import scrapingtools as tools
from constants import *

def has_datatitle(tag):
    """Checks if a tag has 'data-title' in it. Returns Boolean.'"""
    return tag.has_attr("data-title") 

if __name__ == "__main__":
    issuedates = tools.load_list(ERRORS)
    for issue in issuedates:
        try:
            file_parts = issue.split("/")
            file_name = "_".join(file_parts[-2:])+".txt"
            soup = tools.get_soup(issue, filter_=DIVS)
            div_soup = soup.find_all("div")

            for element in div_soup:
                if has_datatitle(element):
                    with open(RANKINGS_DIR+file_name, "a+") as rank_file:
                        rank_file.write(element.get("data-rank"))
                        rank_file.write("\t")                
                        rank_file.write(element.get("data-artist"))
                        rank_file.write("\t")                
                        rank_file.write(element.get("data-title"))
                        rank_file.write("\n")
            print("FINISHED:: ", file_name)
        except:
            print("ERROR:: ", file_name)
            with open(ERRORS_NEW, "a+") as errors:
                errors.write(issue)
                errors.write("\n")
            sleep(6)
