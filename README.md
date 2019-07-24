# simple_python_renamer

## Simple Python Renamer


A small python program that renames raw files to adhere to [Plex-compatible formatting](https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/). This short program can recieve raw, sorted data and format the names into media-server-compatible names.

Example of raw data: ```  "show_title x 0112 - episode.title.for.this.partituclar.episode (1999) (1080p).ext ```

In the above example, Plex or Kodi would read 0112 as "Season 1, Episode 12", when it could really be the 112th episode of a series. The below format is what Plex says is the proper supported naming convention: 

Example of reformatted data: ``` "ShowTitle - S04E25.ext" ```

Adding a ``` (Year) ``` modifier is optional. The year distinction helps Plex determine which show to match to, if there exists another show or movie with a similar or identical name. 

This Simple Python Renamer now has support for TV seasons with over 99 episodes in a single season. 

The script may need to be made executable on your system. Do this with: ```sudo chmod +x simple_python_renamer ```

To run: 
 - Make sure that you meet the pre-conditions below. Call this program with ``` python3 simple_python_renamer ```
 - First, enter the name of the show in the form that as it should appear in proper format.
 - Second, enter the non-relative file-path. Using relative directory names like "." or "../" will work, but they are not recommended. 
 - Third, enter the amount of seasons
 - Fourth, for each season, enter the number of episodes per season

Pre-conditions: 
 - Python3 is installed
 - The code is run on Linux or MacOS
 - The files are sorted in an ascending order. 01 - XX
 - This code requres [natsort](https://github.com/SethMMorton/natsort) - which can be installed by ``` pip3 install natsort ```

