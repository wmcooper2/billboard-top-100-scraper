# Billboard Top 100 Archive Scraper (README not finished)
A CLI tool to scrape song records from www.billboard100.com.

## Purpose
The data will be used to help filter selections already scraped from `www.lyrics.com` as part of a larger project.
The most popular songs have the greatest likelihood of being interesting to EFL students.

### Operation (CLI not finished)
1. Make sure the external database is connected (my personal device "WEEKLY"). (was the old testdata dir?)
2. Run `src/scrape*.py`
3. click the stages from top to bottom.

# Developer Notes
* This program creates directories and writes to files in those created directories.
* Below is some important points for scraping from this site.
* The address system changes a little through the site.
* The saved results, up to but not including the last stage, are always in valid urls (you can copy/paste directly into a browser)
* The last stage's results are plain text files with comma separated values

## Main Process Flow
* scrapeyears.py
* scrapesubcategories.py
* scrapeissues.py
* scraperankings.py

### Scraping Step Notes
1. Main page = https://www.billboard.com/archive/charts
  * major categories by year
  * starts at 1958
  * scrape all "a" tags with this href:
    * "/archive/charts/"
    * example = "/archive/charts/1958"
  * scraping results saved in "/data/yearfin.txt"
  * errors saved in "/data/yearerror.txt"

2. Next page = https://www.billboard.com/archive/charts/1958
  * at the page for each year, there are more categories
  * there can be a few categories or many
  * scrape all "a" tages with this href:
    * "/archive/charts/YEAR/SUBCATEGORY"
    * example = "/archive/charts/1958/r-b-hip-hop-songs"
  * scraping results saved in "/data/subcategoryfin.txt"

3. Next page = https://www.billboard.com/archive/charts/1958/r-b-hip-hop-songs
  * there are issue dates for further subdivision
  * scrape all "a" tags with this href:
    * "/charts/SUBCATEGORY/DATE"
    * example = "/charts/r-b-hip-hop-songs/1958-10-20"
  * scraping results saved in "/data/issuefin.txt"

4. Next page = https://www.billboard.com/charts/r-b-hip-hop-songs/1958-10-20
  * this is the page that has the results I need to scrape
  * it may have less than 100 results because of the category subdivisions
  * This is the element that I need to work with
  * These are the HTML classes (and examples) that I need to pull from
    * data-rank="2" 
    * data-artist="Little Anthony And The Imperials" 
    * data-title="Tears On My Pillow" 

### Other Notes
* This is will be very similar in operation to the Lyric Scraper program. It uses many of the same functions.
