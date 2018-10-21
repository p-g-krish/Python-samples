#!/usr/bin/python

'''
For learning the directory listing
on 21/10/18
'''

import os as system

'''
List the directory and file 
check particular value is file or dir

'''


def listd():
    
      print("Contents of the dir",system.listdir('.'))
      for i in system.listdir('.'):
            print ("iteration value", i)
            if(system.path.isdir(i)):
                 print(i, ",is a directory")
            else:
                print(i,",is a file:status",system.path.isfile(i))
                
                     

listd()
   
