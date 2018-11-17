#/usr/bin/env python3
"""Creates a database with the rankings scraped by 
    .../billboardtop100/src/scraperankings.py
    

    *** This module is meant to run only once (for now, 2018-11-17).
"""

#stand lib
import os
import re
import sqlite3
from pathlib import Path
from pprint import pprint

RANKINGS_DIR = "../rankings"

def addentry(dict_):
    """Adds song entries to the database. Returns None."""
    cursor.execute("INSERT INTO rankings VALUES (?, ?, ?, ?)", 
        (dict_["rank"], dict_["artist"], dict_["song"], dict_["date"]))

def parseline(line):
    """Parses file components. Returns Dictionary."""
    y = line.split("\t")
    return dict(rank=y[0].strip(), artist=y[1].strip(), song=y[2].strip())

if __name__ == "__main__":
    print("STARTING")

    db = "top100.db"
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE rankings (rank text, artist text, song text, date text)")
    files_ = list(Path(RANKINGS_DIR).iterdir())
    filelist = []
    [filelist.append(file_) for file_ in files_ \
        if "album" not in file_.name \
        and "soundtrack" not in file_.name \
        and "airplay" not in file_.name] 
    total = sum(1 for file_ in files_)
    print("TOTAL == ", total)

    current = 1
    for el in filelist:
        name = re.search("\d{4}-\d{2}-\d{2}", el.name)

        with open(el) as file_obj:
            try:
                for x in file_obj.readlines():
                    entry = parseline(x)
                    entry["date"] = name.group(0)
    #                    print(entry)
                    addentry(entry)
            except:
                pass
        # terminal feedback, files finished
        current += 1
        if current % 100 == 0:
            print(str(round((current/total)*100, 4)))

print("FINISHED")
connection.commit()
connection.close()

