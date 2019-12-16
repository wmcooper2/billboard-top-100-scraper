#!/usr/bin/env python3.7
# billboardgui.py
"""GUI tool for scraping data from www.billboard.com"""

# stand lib
from pathlib import Path
import subprocess as sp
from time import sleep
import tkinter as tk
from tkinter import ttk

# custom
from constants import *
from scrapeutil import *
from scrapeyears import scrape as sy
from scrapesubcategories import scrape as ss
from scrapeissues import scrape as si
from scraperankings import scrape as sr

#def redraw_category_values():
#    """Redraws the category values. Returns None."""
#    c_total = ttk.Label(status_frame, 
#        text=str(count_unique_lines(CATEGORY_TODO)))
#    c_total.grid(column=2, row=1, pady=6, padx=6)
#    c_errors = ttk.Label(status_frame, 
#        text=str(count_unique_lines(CATEGORY_ERRORS)))
#    c_errors.grid(column=1, row=1, pady=6, padx=6)
#
#def redraw_artist_values():
#    """Redraws the artist values. Returns None."""
#    a_total = ttk.Label(status_frame, 
#        text=str(total))
#    a_total.grid(column=2, row=2, pady=6, padx=6)
#    a_errors = ttk.Label(status_frame, 
#        text=str(total))
#    a_errors.grid(column=1, row=2, pady=6, padx=6)
#

def draw_y_total():
    """Draws the year total in the GUI. Returns None."""
    y_total = ttk.Label(status_frame, 
        text=str(count_all_lines(YEAR_FIN)))
    y_total.grid(column=2, row=1, pady=6, padx=6)

def years():
    """Begins year scraping. Updates GUI. Returns None."""
    year_sp = sp.run(["python3 scrapeyears.py"], shell=True, 
        stdout=sp.PIPE, encoding="utf-8")
#    year_out = year_sp.stdout
    while process_running(year_sp):
        sleep(2)
        y_total.grid_forget()
        draw_y_total()
        
def process_running(proc):
    """Checks if a process is still running. Returns Boolean."""
    try: 
        proc.poll()
        return True
    except: return False

#Main
#directory_setup()
win = tk.Tk()
win.title("Billboard Top 100 Scraper")

main_box = ttk.Frame(win)
main_box.grid(column=0, row=0, pady=6, padx=6)

address_fr = ttk.LabelFrame(main_box, text="Target", width=L_WIDTH)
address_fr.grid(column=0, row=0, sticky=tk.W, pady=6, padx=6)
address = ttk.Label(address_fr, text=HOME_PAGE)
address.grid(column=0, row=0, sticky=tk.W, pady=6, padx=6)

status_frame = ttk.LabelFrame(main_box)
status_frame.grid(column=0, row=1, pady=6, padx=6)


#headers row
header1 = ttk.Label(status_frame, text="Stages")
header1.grid(column=0, row=0, pady=6, padx=6)
header2 = ttk.Label(status_frame, text="Errors")
header2.grid(column=1, row=0, pady=6, padx=6)
header3 = ttk.Label(status_frame, text="Totals")
header3.grid(column=2, row=0, pady=6, padx=6)


#buttons, left column
y_btn = ttk.Button(status_frame, text="Year", 
#    command=buttontest)
#    command=years)
    command=sy)
y_btn.grid(column=0, row=1, pady=6, padx=6)
s_btn = ttk.Button(status_frame, text="Subcategory", 
    command=buttontest)
s_btn.grid(column=0, row=2, pady=6, padx=6)
i_btn = ttk.Button(status_frame, text="Issue Date", 
    command=buttontest)
i_btn.grid(column=0, row=3, pady=6, padx=6)
r_btn = ttk.Button(status_frame, text="Rank", 
    command=buttontest)
r_btn.grid(column=0, row=4, pady=6, padx=6)


#errors column
y_errors = ttk.Label(status_frame, 
    text=str(count_all_lines(YEAR_ERR)))
y_errors.grid(column=1, row=1, pady=6, padx=6)
s_errors = ttk.Label(status_frame, 
    text=str(count_all_lines(SUB_CATEGORY_ERR)))
s_errors.grid(column=1, row=2, pady=6, padx=6)
i_errors = ttk.Label(status_frame, 
    text=str(count_all_lines(ISSUE_ERR)))
i_errors.grid(column=1, row=3, pady=6, padx=6)
r_errors = ttk.Label(status_frame, 
    text=str(count_all_lines(RANK_ERR)))
r_errors.grid(column=1, row=4, pady=6, padx=6)


#totals column
#y_total = ttk.Label(status_frame, 
#    text=str(count_all_lines(YEARFIN)))
#y_total.grid(column=2, row=1, pady=6, padx=6)
draw_y_total()
s_total = ttk.Label(status_frame, 
    text=str(count_all_lines(SUB_CATEGORY_FIN)))
s_total.grid(column=2, row=2, pady=6, padx=6)
i_total = ttk.Label(status_frame, 
    text=str(count_all_lines(ISSUE_FIN)))
i_total.grid(column=2, row=3, pady=6, padx=6)
r_total = ttk.Label(status_frame, 
    text=str(count_all_lines(RANK_FIN)))
r_total.grid(column=2, row=4, pady=6, padx=6)

#bottom buttons
#button_frame = ttk.LabelFrame(main_box)
#button_frame.grid(column=0, row=2, sticky=tk.W, pady=6, padx=6)

#temp fix
#stop_btn = ttk.Button(button_frame, text="Stop", 
#    command=lambda: quit_(win))
#    command=Stop().stop_scraping)
#stop_btn.grid(column=0, row=0, sticky=tk.W, pady=6, padx=6)

win.mainloop()
