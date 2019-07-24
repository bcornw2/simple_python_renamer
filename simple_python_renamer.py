#!/usr/bin/python3

__author__ = "Benjamin Cornwell"

#yu yu hakusho - s1 = 25  | s2 = 41 | s3 = 28 | s4 = 18

import os
import errno
from natsort import natsorted, ns

def main():


	seasonRange = []
	threeDigits = False
	hasYear = False

	filepath = input("Enter file path for data location - working directory can be relative - \".\"  : ")
	if filepath == '.':
		filepath = os.getcwd()
	print("Working directory for Renamer: " + filepath)
	title = input("Enter formatted title for show - ex. \"Tokyo_Ghoul\" : ")

	list = os.listdir(filepath)
	fileCount = len(list)
	list = natsorted(list, key=lambda y: y.lower())
	print(list)

	try:
		year = int(input("Optional: Enter the Year of production - ex. \"2008\" : "))
	except ValueError:
		year = None
	print("making directory...")
	if year != None:
		hasYear = True 
		titleYr = (title + "_(" + str(year) + ")")
		print("Title is: " + titleYr)
		os.mkdir(titleYr)
		titleDir = titleYr
		
	else:
		hasYear = False
		print("Title is: " + title)
		os.mkdir(title)
		titleDir = title

	seasons = int(input("How many seasons are you naming? : "))
	print("Seasons num: " + str(seasons))
	
	os.chdir(titleDir)
	for i in range(0,seasons):
		dirName = 'Season_{}'.format(i+1)
		print("DIR DIR DIR DIR :::" + os.getcwd())
		try:
			# Create target Directory
			os.mkdir(dirName)
			print("Directory " , dirName ,  " Created ")
		except FileExistsError:
			print("Directory " , dirName ,  " already exists")
	os.chdir(filepath)

	print("=============================== \n==============================")
	print("Current working directory: " + os.getcwd())
	print("Files in this directory: " + str(fileCount))
	print("title directory: " + titleDir)
	print("=============================== \n===============================")


	print("This is the file list: ")
	print(list)	

	for i in range(0,seasons):
		srange = int(input("How many episodes are in season " + str(i+1) + "?: "))
		if srange > 99:
			threedigits = True
		seasonRange.append(srange)

	print("Season Range: ")
	print(seasonRange)

	i=0
	for x in range (0,seasons):
		thisSeason = 'Season_{}'.format(x+1)
		workingDir = os.path.join(filepath,titleDir,thisSeason)
		a = 0
		print("WORKING DIR :::: ")
		print(workingDir)
		print("doing season " + str(x+1) + "...")
		ind = seasonRange[x]
		for y in range (ind):

			newName = title + "_S" + "%02d" % (x+1) + "E" + "%02d" % (y+1) + ".mkv"
			if threeDigits == True:
				dst = os.path.join(filepath,'Season_{}'.format(x+1),title + "_S" + "%02d" % (x+1) + "E" + "%03d" % (y+1) + ".mkv")
			else:
				dst = os.path.join(workingDir,newName)
			
			src = os.path.join(filepath, list[i])
			print("DST ::: " + dst)
			print("SRC ::: " + src)
			print("list[i]: " + list[i])
			os.rename(src, dst)
			print("new file: " + list[i])
			i=i+1

if __name__ == '__main__':
	main()
