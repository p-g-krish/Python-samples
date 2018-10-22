#!/usr/bin/python 

'''
To learning the list data type
on 22/10/18
'''

'''
List operations and basic property handling
'''

a=[]
b=[1,1.3,1+2j]

#Append value into list
def listA(value):
       a.append(value)
       print('value of list a:',a)


'''
Insert frequently used datatypes in to list
for learning purpose
we create a list with some data types int,float,complex,function
And iterate them using for loop and append into the 
the existing list a
'''
def listWithloop(value):
       for i in value:
         print ("value of list",i)
         listA(i)
       print("for loop ended",a)


#Extend the list 
def listext(value):
    a.append("first")
    print("listext",value)
    a.extend(value)
    print("extended list",a)


#Reverse the list
def listR(value):
     print("list reversed called")
     print("before reversed",value)
     value.reverse()
     print("Reversed value",value)


#Copy the existing and assign a list into var
#issues with coping value,may be need to changed
def listCopy(value):
    print("list copy function called",value.copy())
    newList=value.copy()
    print("value of newly copied function",newList)


#Remove the last element from the list
def listRemoveLast(value):
     print("listRemoveLast called",value)
     Removed_element= value.pop()
     print("Current list",value)
     print("removed element",Removed_element)


listRemoveLast(b)     
