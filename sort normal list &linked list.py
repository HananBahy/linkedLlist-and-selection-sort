from time import time
from random import randrange
from linkedlistuno import linkedlistuno
from selectionsort import selectionsort
mylist=[]                       #create empty normal list
mylinkedlist=linkedlistuno()    #create linked list 
for i in range(10000): 
    j=randrange(-1000,1001)
    mylist.insert(0,j)          #insert 10000 item in range(-1000,1001)
    mylinkedlist.add(j)         #add 10000 node  in range(-1000,1001)
    
start1=time()                   #start time of selection sort on normal list
selectionsort(mylist)           #selection sort on array list
end1=time()                     #end time of selection sort on normal list
start2=time()                   #start time of selection sort on linked list
mylinkedlist.selectionsort()    #selection sort on linked list
end2=time()                     #end time of selection sort on linked list

print("time for normal list:",end1-start1) #print Time spent for selection sort on normal list
print("time for linked list:",end2-start2)#print Time spent for selection sort on linked list

 
