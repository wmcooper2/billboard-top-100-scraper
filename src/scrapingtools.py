"""Commonly used scraping tools."""
#stand lib
import re
from time import sleep

#3rd party
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests

#custom
from constants import *

def add_base_url(string):
    """Prepends prefix to string. Returns String."""
    return HOME + string

def persistent_request(url):
    """Makes a single request multiple times until successful.
    Returns Request object."""
    request = requests.get(url)
    if request.status_code == 200:
        return request
    else:
        errors = 0
        while request.status_code != 200 and errors < 3:
            print("BACKING OFF ::", url)
            errors += 1
            sleep(6)
            request = requests.get(url)
            if request.status_code == 200:
                break
        return request

#def get_links(soup_obj, string):
#    """Gets all hrefs containing 'string' from 'soup_obj'. Returns List."""
#    return soup_obj.find_all(href=re.compile(string))

#def get_soup(link, filter_=None):
#    """Gets soup from a link. Returns BeautifulSoup object."""
#    request = persistent_request(link)
#    return BeautifulSoup(request.content, "html.parser", parse_only=filter_)

def get_div_soup(link):
    """Gets soup from a link. Returns BeautifulSoup object."""
    request = persistent_request(link)
    return BeautifulSoup(request.content, "html.parser", parse_only=DIVS)

#def get_href(a_element):
#    """Gets the href value from the a-tag element. Returns String."""
#    return a_element.get("href")

#def save_list(list_, location):
#    """Saves 'list_' contents to 'location' as plain text file.
#        Returns None."""
#    with open(location, "a+") as file_obj:
#        for element in list_:
#            file_obj.write(get_href(element))
#            file_obj.write("\n")

def save_link_list(list_, location):
    """Saves 'list_' contents to 'location' as plain text file.
        Returns None."""
    with open(location, "a+") as file_obj:
        for element in list_:
            file_obj.write(element)
            file_obj.write("\n")

def load_list(location):
    """Loads a list of elements from a text file. Returns List."""
    temp = []
    with open(location, "r") as file_obj:
        for line in file_obj.readlines():
            temp.append(line.strip())
    return temp
