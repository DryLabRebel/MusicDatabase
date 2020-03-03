
So I want to:

- figure out how I'm going to structure my database
- figure out how to get the data into it
- use it as a platform to learn SQL, python, whatever else

I want to create a database to catalogue my music collection, in a way that forces me to learn some python and SQL.

I can probably even run some basic statistical analyses on my data as well

- Some linear modelling and other simple analyses

Database design
---------------

From [NTU](https://www.ntu.edu.sg/home/ehchua/programming/sql/Relational_Database_Design.html).

### Database design objective ###

- Eliminate redundancy: do not duplicate data. Duplicates require extra storage and make a database inconsistent and unmanageable.
- Ensure Data Integrity

### Define the purpose ###

The purpose is to catalogue my music collection in a meaningful way.

### Primary Keys ###

- song + artist + album? - this would ensure that any song that appeared under the same artist, on the same album would be a duplicate, and I could remove it
    - this is assuming that different versions of the same song are identified (live, acoustic, explicit, etc.)
    - I could specify the recording format separately? Some songs might have multiple formats (live AND explicit?)
    - I could have separate columns formatA, formatB, formatC?
- I think in that case it might be easier to just have a unique ID number for each song?
    - This could be a code based on `artist_album_disk_trackNO` something like XXXX-XXX-X-XX

- I could have a primary table:

    ID    track artist    album disk track_no length    rating    file_location date_added    date_updated

*NO* - this is bad. I need to *normalise* this idea.

Song Table:

    ID track length rating file_location date_added date_updated

Artist table:

    ID artist

Album table

    artist album

Note: Here, album can have an ID that's unique only within the artist

- Then other useful tables

    artist    album genre subgenre

Or something like that.

Or, maybe artist ID, should be my primary key!

    artistID    artist  albumID

    albumID album

    albumID track_no   track

    trackID length  rating  date_added  

    artistID  genre

    genre subgenre

***OK, now we're getting somewhere***

How do I turn this into a Datbase? Done.

Where is all the information for my Music library?
  - How do I find and access the metadata for my Music library?

    mdls path/to/filename

