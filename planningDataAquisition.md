Data Aquisition
===============

This is the information I need:

    artist, album, release_year, track_no, title, composer, length, rating, filename, date_added, genre, subgenre

These are my primary and secondary keys:

    artistID	albumID trackID genre	subgenre

How do I find and access the metadata for my Music library?

Bash:

    mdls path/to/filename

Python:

    ???

Could I pipe the bash command into a python scipt which parses the information and feeds it into an SQL script, which automatically updates a database?

What do I want to do now?

Start building my tables?

How? If I want to reinforce some of the most basic SQL commands, I could go through one at a time and just start adding song info by hand... seriously?

OK - not a bad idea actually. Would be the easiest way to get started. But I also want to work on my python/aquisition skills

Otherwise I could write a simple (simple?) python or bash (or perl, or awk) script which mines my Music directory for all the information I need, and automatically fills tables according to my specifications?

Oh man, I don't even know where to start.

If I wanted to learn python, this is my first real opportunity

What do I want to do?

Suppose I wanted to mine the information using a python script.

I can then either
- save all the information as .txt dataframes - then use SQL to add these tables to my music database?
- feed this into a SQL script which automatically adds/updates the information to the relevant tables

How would I even start?

- Learn some python?
- Just get started?

*I need to learn some SQL*
*I need to learn some python*

Here's a great stack question to get you started:

        https://stackoverflow.com/questions/8948/accessing-mp3-metadata-with-python

OK, so there's `eyeD3` and `mutagen`. Apparently both python libraries (packages?), both parse metadata.

What am I thinking about?

Here's what I need:

    table1	artistID	artist	albumID
    table2	albumID	album	releast_year
    table3	albumID	track_no	trackID
    table4	trackID	title	composer	length	rating	filename	date_added	
    table5	artistID	genre
    table6	genre	subgenre

    artist, album, release_year, track_no, title, composer, length, rating, filename, date_added, genre, subgenre

Could get away with:

*Check* (15-03-2021) - artist
*Check* (15-03-2021) - album
*Check* (15-03-2021) - release_year
*Check* (15-03-2021) - track_no
*Check* (15-03-2021) - title
*Check* (15-03-2021) - length
*Check* (15-03-2021) - filename
*Check* (15-03-2021) - date_added
*Check* (15-03-2021) - genre

- mdls doesn't give me all the info I'm looking for. It's more system info.

Example:

    /Users/geoff/Music/iTunes/iTunes Media/Music/Ahrix/Nova - Single/01 Nova.m4a
    kMDItemAlbum                           = "Nova - Single"
    kMDItemAlternateNames                  = (
        "01 Nova.m4a"
    )
    kMDItemAudioBitRate                    = 262669
    kMDItemAudioChannelCount               = 2
    kMDItemAudioSampleRate                 = 44100
    kMDItemAudioTrackNumber                = 1
    kMDItemAuthors                         = (
        Ahrix
    )
    kMDItemContentCreationDate             = 2018-05-11 22:56:07 +0000
    kMDItemContentCreationDate_Ranking     = 2018-05-11 00:00:00 +0000
    kMDItemContentModificationDate         = 2020-03-02 03:32:02 +0000
    kMDItemContentModificationDate_Ranking = 2020-03-02 00:00:00 +0000
    kMDItemContentType                     = "com.apple.m4a-audio"
    kMDItemContentTypeTree                 = (
        "com.apple.m4a-audio",
        "public.mpeg-4-audio",
        "public.audio",
        "public.audiovisual-content",
        "public.data",
        "public.item",
        "public.content"
    )
    kMDItemCopyright                       = "℗ 2017 Ahrix"
    kMDItemDateAdded                       = 2018-05-11 22:56:12 +0000
    kMDItemDateAdded_Ranking               = 2018-05-11 00:00:00 +0000
    kMDItemDisplayName                     = "Nova"
    kMDItemDocumentIdentifier              = 0
    kMDItemDurationSeconds                 = 281.32589569161
    kMDItemFSContentChangeDate             = 2020-03-02 03:32:02 +0000
    kMDItemFSCreationDate                  = 2018-05-11 22:56:07 +0000
    kMDItemFSCreatorCode                   = "hook"
    kMDItemFSFinderFlags                   = 0
    kMDItemFSHasCustomIcon                 = (null)
    kMDItemFSInvisible                     = 0
    kMDItemFSIsExtensionHidden             = 0
    kMDItemFSIsStationery                  = (null)
    kMDItemFSLabel                         = 0
    kMDItemFSName                          = "01 Nova.m4a"
    kMDItemFSNodeCount                     = (null)
    kMDItemFSOwnerGroupID                  = 20
    kMDItemFSOwnerUserID                   = 501
    kMDItemFSSize                          = 9847512
    kMDItemFSTypeCode                      = ""
    kMDItemInterestingDate_Ranking         = 2020-03-02 00:00:00 +0000
    kMDItemKind                            = "Apple MPEG-4 audio"
    kMDItemLogicalSize                     = 9847512
    kMDItemMediaTypes                      = (
        Sound
    )
    kMDItemMusicalGenre                    = "Dance"
    kMDItemPhysicalSize                    = 10502144
    kMDItemPurchaseDate                    = 2018-05-11 12:56:07 +0000
    kMDItemRecordingYear                   = 2013
    kMDItemTitle                           = "Nova"
    kMDItemTotalBitRate                    = 262669

---

It has enough... enough for now.

Also I found this:

    import os

    #print(os.stat(os.path.join("/Users/geoff/Music/iTunes/iTunes Media/Music/Ahrix/Nova - Single/", "01 Nova.m4a")))

    import subprocess

    filename = "/Users/geoff/Music/iTunes/iTunes Media/Music/Calvin Harris/Motion/06 Outside (feat. Ellie Goulding).m4a"

    p = subprocess.run(["mdls", filename], capture_output=True, text=True)

    print(p.stdout)

Ooooooh!!

It's just calling bash commands from a python script, but if I had just resorted to bash, that's what I would've done anyway.

This is probably also very general, and may allow me to do other fancy bash stuff in python!

Even better is tinytag - a python package with reads file meta data. Bingo!!

Now what?




