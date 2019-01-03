"""Scrape song rankings from www.billboard.com."""
#custom
from constants import *
from scrapeutil import *

def has_datatitle(tag):
    """Checks if a tag has 'data-title' in it. Returns Boolean.'"""
    return tag.has_attr("data-title") 

def format_file_name(url):
    """Formats a file name. Returns String."""
    file_parts = url.split("/")
    return "_".join(file_parts[-2:])+".txt"

def save_ranking(file_, div_el):
    """Appends ranking to 'file'. Returns None."""
    with open(RANKINGDIR+file_, "a+") as f:
        f.write(div_el.get("data-rank"))
        f.write(",")                
        f.write(div_el.get("data-artist"))
        f.write(",")                
        f.write(div_el.get("data-title"))
        f.write("\n")

def scrape():
    """Scrapes rankings from www.billboard.com. Returns None."""
    print("--- RANK SCRAPING, STARTED --- ")
    todo, finished = scrape_setup(ISSUEFIN, RANKERROR, RANKFIN)
    fin_len     = len(finished)
    todo_len    = len(todo)
    print("finished:", fin_len)
    print("todo    :", todo_len)

    rank_count = 0
    for link in sorted(todo):
        try:
            soup = get_soup(link, filter_=DIVS)
            div_soup = soup.find_all("div")
            for element in div_soup:
                if has_datatitle(element):
                    name = format_file_name(link)
                    save_ranking(name, element)
            print("Saved:: ", name)
            save_append_line(link, RANKFIN)
            rank_count += 1
        except:
            print("Error:", link)
            save_append_line(link, RANKERROR)
    print("rank_count:", str(rank_count))
    print("--- RANK SCRAPING, FINISHED --- ")

if __name__ == "__main__":
    scrape()
