# simple_python_renamer

## Simple Python Renamer


A small python program that renames raw files to adhere to plex-compatible formatting. This short program can recieve raw, sorted data and format the names into media-server-compatible names.

Example of raw data:  "show_title x 0112 - episode.title.for.this.partituclar.episode (1999) (1080p)"

Example of reformatted data: "Show_title_S04E25"

Titles in this notation are readable by popular home media server platforms like Plex and Kodi. 

This Simple Python Renamer now has support for TV seasons with over 99 episodes in a single season. In such cases, the formatting with change from {01..99} to {001..999}.

To run: 
 - First, enter the name of the show in the form that as it should appear in proper format.
 - Second, enter the non-relative file-path. Using relative directory names like "." or "../" will work, but they are not recommended. 
 - Third, enter the amount of seasons
 - Fourth, for each season, enter the number of episodes per season

Pre-conditions: 
 - Python3 is installed
 - The code is run on Linux or MacOS
 - The files are sorted in an ascending order. 01 - XX
