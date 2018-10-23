#!/usr/bin/python 

'''
To learning the list data type
on 22/10/18
'''

'''
List operations and basic property handling
implemented methods
1.append
2.extend
3.reverse
4.copy
5.pop
6.clear
7.count
8.index
9.insert
10.remove
---Need to implement
11.sort
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


#coded on 23/10/18
#To remove all element from the list
def gonnaEmpty(list):
     print ("before clearing",list)
     list.clear()
     print("Cleared the list",list)

 
#count the letter or word from the list
def countWordFromList(list, word):
      print("list",list,"word", word)
      count=list.count(word)
      print("count of ",word, "is",count)
        

#get Index of value from the list
#Element should be inthe list
def getIndex(list,element):
    print("list",list,"element",element)
    index=list.index(element)
    print("index value of ",element, "is ",index)


#index value into particular index
def InsertNthIndex(list,index,value):
    print("before insert",list)
    list.insert(index,value)
    print("after insert",list)

#example call
#InsertNthIndex(b,0,"test")


#Remove the particular element from the array
def removeElement(list,element):
    print("before remove",list)
    list.remove(element)
    print("after remove",list)

removeElement(b,1)
