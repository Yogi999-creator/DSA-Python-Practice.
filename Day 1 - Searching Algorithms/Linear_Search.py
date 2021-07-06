# Linear Search Algorithm Implementation in Python.
# @code by: Mundhra Yogesh Pawan.

def Linear_Search(Array , Target):
    
    for i in range (len(Array)):
        if Array[i] == Target:
            return i        
    return -1

Array = [20,50,30,10,40]
Target = 30

A = Linear_Search(Array,Target)
if (A != -1):
    print(Target, "is at index", A)
else:
    print(Target, "is not found in the Array.")    