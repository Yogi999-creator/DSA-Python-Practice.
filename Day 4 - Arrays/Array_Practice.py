# Traversing, Accessing, Inserting, Deleting, Searching, Updating Array. (Python Implementation)
# @code by: Mundhra Yogesh Pawan.

from array import *

myarray = array('i', [10,20,30,40,50])

print("Traversing the array...")
for x in myarray:
    print(x)

print("Accessing array element...")
print (myarray[0])
print (myarray[2])

print("Inserting element in array...")
myarray.insert(1,60)
for x in myarray:
    print(x)

print("Deleting element in array...")
myarray.remove(40)
for x in myarray:
    print(x)

print("Searching index of an element...")
myarray = array('i', [10,20,30,40,50])
print (myarray.index(40))

print("Update an element in array...")
myarray[2] = 80
for x in myarray:
    print(x)