#!/usr/bin/python3

#TODO
#add support for different video file types or different containers


# According to Plex.tv's official support page, files that are listed for any television
# viewing should be formatted in the following convention:
# 		/TVShows/Showname (opt. Year)/ ShowName - S02E17.ext
# source: https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/
#This program will take raw, but numerically sorted data, and format that into place.
#Formatting can use spaces, but other special characters are not recommended by Plex

__author__ = "Benjamin Cornwell"

# Requires pip3 install natsort - native Python sorting is not tenable for programs that
# demand accuracy for file order.

import os
import errno
from natsort import natsorted, ns

def main():


	seasonRange = []
	threeDigits = False
	hasYear = False

	print("Simple Python Renamer: A small and fast program that can rename your files to comply with Plex or Kodi naming requirements")

	# Prompt user for input for construction
	filepath = input("Enter file path for data location - working directory can be relative - \".\"   >> ")
	if filepath == '.':
		filepath = os.getcwd()
	print("Working directory for Renamer: " + filepath)
	title = input("Enter formatted title for show - ex. \"Tokyo Ghoul\"   >> ")

	# natsort - 3rd party module - sorts list by [1,2,3..10,11..100,101]
	# instead of [1,10,100,101,etc]
	list = os.listdir(filepath)
	fileCount = len(list)
	list = natsorted(list, key=lambda y: y.lower())
	print("This is a list of all files in working directory: " + str(list))

	# Support for Year - appears in title directory only
	print("The (Year) indicator in the title is optional, and is only used to differentiate two shows of the same name")
	print("Press [ENTER] to bypass (Year) designation and proceed to renaming")
	try:
		year = int(input("Optional: Enter the Year of production - ex. \"2008\"   >> "))
	except ValueError:
		year = None

	print("making directory...")

	# Constructing title directory - e.g. "Cops (1999)/"
	# With or without year
	if year != None:
		hasYear = True
		titleYr = (title + " (" + str(year) + ")")
		print("Title is: " + titleYr)
		os.mkdir(titleYr)
		titleDir = titleYr
	else:
		hasYear = False
		print("Title is: " + title)
		os.mkdir(title)
		titleDir = title

	seasons = int(input("How many seasons are you naming?   >> "))
	print("Seasons num: " + str(seasons))

	# Create a directory for each season, to specify season separation.
	# Changes working directory to the titleDir, makes the Season_i
	#directories, and then changes back to the original working dir.
	os.chdir(titleDir)
	for i in range(0,seasons):
		dirName = 'Season {}'.format(i+1)
		try:
			# Create target Directory
			os.mkdir(dirName)
			print("Directory " , dirName ,  " Created ")
		except FileExistsError:
			print("Directory " , dirName ,  " already exists")
	os.chdir(filepath)

	#dramatic diagnostics - mostly used for testing during writing
	print("=+============================== \n==============================")
	print("Working directory: " + os.getcwd())
	print("Files in data directory: " + str(fileCount))
	print("title directory: " + titleDir)
	print("=============================== \n===============================")

	# Creates array of each season's episode count. If a single season of a show has
	#more than 99 episodes, this will toggle a switch to reconfigure the file title
	# - e.g. "Cops_S01E03.mkv" to be triple-count on E - e.g. "Cops_S01E104.mkv"
	for i in range(0,seasons):
		srange = int(input("How many episodes are in season " + str(i+1) + "?   >> "))
		if srange > 99:
			threedigits = True
		seasonRange.append(srange)

	# i = epsiode count, or index of each file - before and after os.rename function
	# Nested for loops allow processing of each Season directory first, then the drill
	# down to depth=2 and rename and mv the files the their proper Season location
	i=0
	for x in range (0,seasons):
		thisSeason = 'Season {}'.format(x+1)
		workingDir = os.path.join(filepath,titleDir,thisSeason)
		a = 0
		print("doing season " + str(x+1) + "...")
		ind = seasonRange[x]
		for y in range (ind):
			if threeDigits == True:
				newName = title + " - S" + "%02d" % (x+1) + "E" + "%03d" % (y+1) + ".mkv"
			else:
				newName = title + " - S" + "%02d" % (x+1) + "E" + "%02d" % (y+1) + ".mkv"
			dst = os.path.join(workingDir,newName)
			src = os.path.join(filepath, list[i])
			os.rename(src, dst)
			print("new file: " + src)
			i=i+1

if __name__ == '__main__':
	main()
