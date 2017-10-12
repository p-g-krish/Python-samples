'''
Script for  Checking the file extension [ pdf and Xlsx ]
python version 2.7

'''

import sys


#File extenstion check
def check_ext(filename,ext):
	for x in filename:
	 
	    print "check the ext ",x
	    
	    #Extension check 
	    if(x.endswith(tuple(ext))):
	   	   print "Success connection with files"
	   	
	    else:
	   	   print "file %s is not authorized xlsx files" % x
                   sys.exit("File extension not allowed")


if __name__ ==  "__main__":
	filename=['data.pdf','data.pf','data.pd', 'data.xlsx', 'data.Xlsx']
	
	#assign the ext type 
	ext=['.pdf','.xlsx','.Pdf','.Xlsx']
        
        #call File extension file check
        
        check_ext(filename,ext)
       
