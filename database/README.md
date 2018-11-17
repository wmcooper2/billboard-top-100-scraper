# Billboard Top 100 Database

### Purpose

To collect the basic information about the songs in a database.
To get just enough (doesn't need to be a 100% complete list) data for the next project.

### Database fields

* Song name
* Album name
* Artist
* Date (of issue)
* Rank on charts

### Operation

* run `python3 billboardtop100/database/addrankings.py`
  * The result is a database "top100.db" that has about 2.7 million records
  * each record has;
    * rank (of whatever list is was in which is irrelevant for my next project)
    * artist name
    * song name
    * date (of ranking issuance)
