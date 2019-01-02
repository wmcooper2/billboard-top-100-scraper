# Billboard Top 100 Archive Scraper (README not finished)
A GUI tool to scrape the hit song records from www.billboard100.com.

## Purpose
The data will be used to help filter selections already scraped from `www.lyrics.com` as part of a larger project.
The most popular songs have the greatest likelihood of being interesting to EFL students.

### Process Flow
* scrapeyears.py
  * makesubcategorylinks.py (to prepare for 'scrapesubcategories.py')
* scrapesubcategories.py
* scrapeissues.py
* scraperankings.py

### Operation
1. start the GUI
2. click the stages from top to bottom.

### Scraping Steps
1. Main page = https://www.billboard.com/archive/charts
  * major categories by year
  * starts at 1958
  * scrape all "a" tags with this href:
    * "/archive/charts/"
    * example = "/archive/charts/1958"
  * scraping results saved in "/data/years.txt"

1. A. combine makeyearlinks.py with scrapeyears.py
  * combine years.txt with yearlinks.text

2. Next page = https://www.billboard.com/archive/charts/1958
  * at the page for each year, there are more categories
  * there can be a few categories or many
  * scrape all "a" tages with this href:
    * "/archive/charts/YEAR/SUBCATEGORY"
    * example = "/archive/charts/1958/r-b-hip-hop-songs"
  * scraping results saved in "/data/subcategories.txt"

3. Next page = https://www.billboard.com/archive/charts/1958/r-b-hip-hop-songs
  * there are issue dates for further subdivision
  * scrape all "a" tags with this href:
    * "/charts/SUBCATEGORY/DATE"
    * example = "/charts/r-b-hip-hop-songs/1958-10-20"
  * scraping results saved in "/data/issuelinks.txt"

4. Next page = https://www.billboard.com/charts/r-b-hip-hop-songs/1958-10-20
  * this is the page that has the results I need to scrape
  * it may have less than 100 results because of the category subdivisions
  * This is the element that I need to work with
  * These are the HTML classes (and examples) that I need to pull from
    * data-rank="2" 
    * data-artist="Little Anthony And The Imperials" 
    * data-title="Tears On My Pillow" 

### Other Notes
* This is will be very similar in operation to the Lyric Scraper program.
* There are some differences with how the data is formatted from the billboard website (XML)

### Developer Notes
* This program creates directories and writes to files in those created directories.
