#!/usr/bin/python3

#yu yu hakusho - s1 = 25  | s2 = 41 | s3 = 28 | s4 = 18

import os
import os.path
#import array as seasonRange
#import array as filelist

def main():


	title = raw_input("Enter formatted title for show: ")
	print("Title is: " + title)
	filepath = raw_input("Enter non-relative file path for data location: ")
	print(filepath)
	seasons = input("How many seasons? : ")
	seasonRange = []
	print("Seasons num: " + str(seasons))
	for i in range(0,seasons):
		srange = input("How many episodes are in season " + str(i+1) + "?: ")
		seasonRange.append(srange)
##	for y in seasonRange:
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
			src = os.path.join(filepath, list[i])
			dst = os.path.join(filepath, title + "__S" + "%02d" % (x+1) + "E" "%02d" % (y+1) + ".mkv")
			print("DST :::" + dst)
			os.rename(src, dst)
			i=i+1


#	list2 = os.listdir(filepath)
#	print(list2)



##	for filename in os.listdir("/media/sda/downloads/test"):
##		dst = "Yu Yu Hakusho S" + "%02d" % x + "E" + "%02d" % i + ".mkv"
##		os.rename(filename, dst)
###		i += 1


if __name__ == '__main__':
	main()
