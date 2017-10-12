#!/usr/bin/python
#Get inode id for zurik testing

import os


def get_inode():
	arr=os.listdir(os.getcwd())
	
	
	for i in arr:
	   print "For checking inode id", i
	   #print the inode number
	   S=os.stat(i).st_ino
	   print 'S', S
	   print  os.stat(i).st_ino


def main():
     print "from the main"
     get_inode()

if __name__ == '__main__':
    print "call the main"
    main()
