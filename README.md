# simple_python_renamer

##Simple Python Renamer


A small python program that renames raw files to adhere to plex-compatible formatting. This short program can recieve raw, sorted data and format the names into media-server-compatible names.

Example of raw data:  "show_title x 0112 - episode.title.for.this.partituclar.episode (1999) (1080p)

Example of reformatted data: "Show_title_S04E25"

Titles in this notation are readable by popular home media server platforms like Plex and Kodi. 

To run: 
 - First, enter the name of the show in the form that as it should appear in proper format.
 - Second, enter the non-relative file-path. Using relative directory names like "." or "../" will work, but they are not recommended. 
 - Third, enter the amount of seasons
 - Fourth, for each season, enter the number of episodes per season

Pre-conditions: 
 - Python3 is installed
 - The code is run on Linux or MacOS
