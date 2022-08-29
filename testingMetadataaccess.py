import os

#print(os.stat(os.path.join("/Users/geoff/Music/iTunes/iTunes Media/Music/Ahrix/Nova - Single/", "01 Nova.m4a")))

import subprocess

filename = "/Users/geoff/Music/iTunes/iTunes Media/Music/Calvin Harris/Motion/06 Outside (feat. Ellie Goulding).m4a"

p = subprocess.run(["mdls", filename], capture_output=True, text=True)

print(p.stdout)

# Also

# Import Tinytag method from
# tinytag library
from tinytag import TinyTag

# Pass the filename into the
# Tinytag.get() method and store
# the result in audio variable
audio = TinyTag.get(filename)

# Use the attributes
# and Display

print("Title:" + audio.title)

print("Artist: " + audio.artist)

print("Genre:" + audio.genre)

print("Year Released: " + audio.year)

print("Bitrate:" + str(audio.bitrate) + " kBits/s")

print("Composer: " + audio.composer)

print("Filesize: " + str(audio.filesize) + " bytes")

print("AlbumArtist: " + audio.albumartist)

print("Duration: " + str(audio.duration) + " seconds")

print("TrackTotal: " + str(audio.track_total))

