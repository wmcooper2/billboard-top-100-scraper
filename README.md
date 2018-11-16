# Billboard Top 100 Archive Scraper

Get the data for the top 100 songs since 1958 and store the data in text files.

## Purpose

The data will be used to pick the most popular songs from the already scraped lyrics data from `www.lyrics.com`.

The most popular songs have the greatest likelihood of being interesting to EFL students.

This way, the most relevant songs from the lyrics database will be determined to have a higher priority when looking for matching grammar patterns to make customized English lessons for students.

The most popular songs are more likely to have a music video or other performance on Youtube that can be found compared to the least popular songs (ones that don't show up on the Billboard Top 100).

### Process Flow
* scrapeyears.py
  * makesubcategorylinks.py (to prepare for 'scrapesubcategories.py')
* scrapesubcategories.py
* scrapeissues.py
* scraperankings.py
  * recoverrankings.py (only for recovering at the final step)

### Error recovery

Recovery at the final stage;  
* Errors that occur when running 'scraperankings.py' are recovered by replacing the parameter on line 21 (for now)
* Don't forget to rename for the new error file in 'constants.py'
