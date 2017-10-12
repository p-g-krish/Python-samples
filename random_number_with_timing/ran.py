import threading
import random

'''
print the random number on every 5 secs 
the random number between 1,1000
'''
def printit():
    
    threading.Timer(5.0, printit).start()
    print "hai"
    r=random.randint(1,1000)
    print "to check the random %d" % r

printit()

