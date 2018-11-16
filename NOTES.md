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
