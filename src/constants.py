"""Constants for Billboard Top 100 scraping program."""
#stand lib
from pathlib import Path

#3rd party
from bs4 import SoupStrainer

#Program dirs/files
CWD                 = str(Path().cwd())
A_TAGS              = SoupStrainer("a")
DIVS                = SoupStrainer("div")
DATADIR             = CWD+"/../data/"

ERRORS              = CWD+"/../errors.txt"
ERRORS_NEW          = CWD+"/../errors_new.txt"
RANKINGS_DIR        = CWD+"/../rankings/"

ISSUEERROR          = DATADIR+"issueerror.txt"
ISSUEFIN            = DATADIR+"issuefin.txt"
SUBCATEGORYERROR    = DATADIR+"subcategoryerror.txt"
SUBCATEGORYFIN      = DATADIR+"subcategoryfin.txt"
YEARERROR           = DATADIR+"yearerror.txt"
YEARFIN             = DATADIR+"yearfin.txt"

#urls
HOMEPAGE            = "https://www.billboard.com"
YEARSPAGE           = HOMEPAGE+"/archive/charts"

