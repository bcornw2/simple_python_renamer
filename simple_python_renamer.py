#!/usr/bin/python3

__author__ = "Benjamin Cornwell"

#yu yu hakusho - s1 = 25  | s2 = 41 | s3 = 28 | s4 = 18

import os
import os.path

def main():


	seasonRange = []
	threeDigits = None

	title = raw_input("Enter formatted title for show: ")
	print("Title is: " + title)
	filepath = raw_input("Enter non-relative file path for data location: ")
	print(filepath)
	seasons = input("How many seasons? : ")
	print("Seasons num: " + str(seasons))
	for i in range(0,seasons):
		srange = input("How many episodes are in season " + str(i+1) + "?: ")
		if srange > 99:
			threedigits = True
		seasonRange.append(srange)

	print(seasonRange)

	list = os.listdir(filepath)
	file_count = len(list)
	print file_count
	i=0
	for x in range (0,seasons):
		a = 0
		print("doing season " + str(x+1) + "...")
		ind = seasonRange[x]
		for y in range (ind):

			if threeDigits == True:
				dst = os.path.join(filepath, title + "_S" + "%02d" % (x+1) + "E" + "%03d" % (y+1) + ".mkv")
			else:
				dst = os.path.join(filepath, title + "_S" + "%02d" % (x+1) + "E" + "%03d" % (y+1) + ".mkv")
			src = os.path.join(filepath, list[i])
			print("DST :::" + dst)
			os.rename(src, dst)
			i=i+1

if __name__ == '__main__':
	main()
