#Additional, optional package to facilitate moving files from one season to the next. 

#!usr/bin/python3

import glob, os

print(os.getcwd())
for i in (glob.glob("./*Adventure Time*")):
        print(" === orig. === "+i)
        num = int(i[21]+i[22])
        print(num)
        new_num = num+13
        print(new_num)
        os.rename(i, i.replace(str(num), str(new_num), 1))
        print(" === .new. ===" + i)
        print("=====================================================")

#print(glob.glob("./*Adventure Time*"))

