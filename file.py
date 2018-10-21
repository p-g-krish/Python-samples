#!/usr/bin/python


'''
For Teaching file handling in python
on 21/10/18
by kumar
'''

'''
File handling functions

'''

#Create and write into the file
def fw():
   a=open("Data.txt", "w")
   a.write("firstline\nMiddleline\nlastLine\n")
   a.close()

#Read from  file
def fr():
    a=open("Data.txt","r")
    print("Reading the content of data file\n",  a.read())
    a.close()

#Append data into the files
def fa():
    a=open("Data.txt","a")
    a.write("Appended text\n")
    a.close()


#Read the first line only
def frf():
    a=open("Data.txt", "r")
    print("Reading the first line\n", a.readline())
    a.close()

#Read multiple lines 
def frm():
    a=open("Data.txt", "r")
    print("Reading multiple lines ------->\n",a.readlines()[-1])
    a.close()
frm()
