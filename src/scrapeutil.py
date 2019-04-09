#!/usr/bin/env python3.7
# billboardgui.py
"""Utility module Lyric Scraper program."""

# stand lib
import json
from pathlib import Path
import re
import subprocess as sp
from time import sleep
from typing import Text
from typing import Tuple

# 3rd party
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests

# custom
from constants import HOME_PAGE
from constants import SLEEP_TIME

filter_ = SoupStrainer("a")


def buttontest() -> None:
    """Prints test line to terminal. Returns None."""
    print("button works")
    return None


def ensure_exists(string: Text) -> None:
    """Makes 'string' dir if doesn't exist. Returns None."""
    if not Path(string).exists():
        Path(string).mkdir()
    return None


def count_all_lines(file_):
    """Counts all lines in file_. Returns Integer."""
    with open(file_, "r") as f:
        return len(f.readlines())


def count_files(dir_: Text) -> int:
    """Counts files in 'dir_'. Returns Integer."""
    path = str(Path(dir_))
    cmd = "ls "+path+" | wc -l"
    return sp.run(cmd, encoding="utf-8", shell=True,
        stdout=sp.PIPE, stderr=sp.PIPE).stdout.strip()


def count_unique_lines(file_):
    """Counts unique lines in 'file_'. Returns Integer."""
    with open(file_, "r") as f:
        return len(set(f.readlines()))


def format_artist_link(href):
    """Formats URL for the artist. Returns String."""
    return HOME_PAGE+"/"+href.get("href")


def format_file_name(url):
    """Formats a file name. Returns String."""
    file_parts = url.split("/")
    return "_".join(file_parts[-2:])+".txt"


def format_regex_string(year: Text) -> Text:
    """Formats regex string. Returns String."""
    return "\/archive\/charts\/"+year+"\/"


def get_hrefs(linklist):
    """Gets all href values from 'linklist'. Returns List."""
    return list(map(lambda link: link.get("href"), linklist))


def get_links(soup, string):
    """Gets hrefs containing 'string' from 'soup'. Returns List."""
    return soup.find_all(href=re.compile(string))


def get_soup(link, filter_=None):
    """Gets soup from a link. Returns BeautifulSoup object."""
    request = persistent_request(link)
    return BeautifulSoup(request.content, "html.parser", 
        parse_only=filter_)


def get_year(url):
    """Gets the year from 'url'. Returns String"""
    return str(Path(url).parts[-1])


def has_data_title(tag):
    """Checks if a tag has 'data-title' in it. Returns Boolean.'"""
    return tag.has_attr("data-title") 


def load_file_list(file_: Text) -> List[Text]:
    """Loads 'file_'. Returns List."""
    with open(file_, "r") as f:
        return [line.strip() for line in f.readlines()]


def persistent_request(link):
    """Persistently makes a request. Returns Request object."""
    request = simple_request(link)
    if not request.status_code == 200:
        return three_requests(link)
    return request


def save(list_, location):
    """Writes 'list_' to 'location' as txt file. Returns None."""
    with open(location, "w+") as f:
        for element in sorted(list_):
            f.write(element)
            f.write("\n")


def save_lyrics(list_, location):
    """Writes 'list_' to 'location' as txt file. Returns None."""
    with open(location, "w+") as f:
        for element in list_:
            f.write(element)
            f.write("\n")


def save_append(list_, location):
    """Appends 'list_' to 'location' as txt file. Returns None."""
    with open(location, "a+") as f:
        for element in list_:
            f.write(element)
            f.write("\n")


def save_append_line(string, location):
    """Appends 'string' to location's text file. Returns None."""
    with open(location, "a+") as f:
        f.write(string)
        f.write("\n")


def save_ranking(file_, div_el):
    """Appends ranking to 'file'. Returns None."""
    with open(RANKING_DIR+file_, "a+") as f:
        f.write(div_el.get("data-rank"))
        f.write(",")                
        f.write(div_el.get("data-artist"))
        f.write(",")                
        f.write(div_el.get("data-title"))
        f.write("\n")


def scrape_setup(prev_fin: Text,
                 cur_fin: Text) -> Tuple[List[Text], List[Text]]:
    """Determines which links need to be scraped. 
        needs;
            - previous stage finished file
            - current stage finished file
        Returns 2 Lists."""
    todo = set(load_file_list(prev_fin))
    finished = set(load_file_list(cur_fin))
    return (todo.difference(finished), list(finished))


def simple_request(link):
    """Makes only one request attempt. Returns Request object."""
    return requests.get(link)

    
def three_requests(link):
    """Makes up to 3 request attempts. Returns Request object."""
    errors = 0
    request = simple_request(link)
    while request.status_code != 200 and errors < 3:
        print("BACKING OFF {0} :: {1}".format(SLEEP_TIME, link))
        errors += 1
        sleep(SLEEP_TIME)
        request = simple_request(link)
        if request.status_code == 200:
            break
    return request
