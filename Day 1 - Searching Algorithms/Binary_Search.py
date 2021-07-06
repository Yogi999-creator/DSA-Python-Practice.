# Binary Search Algorithm Implementation in Python.
# @code by: Mundhra Yogesh Pawan.

def Binary_Search (Array, LB , UB , Target):
   
    while (LB <= UB):
        Middle = (LB + UB) // 2
        if Array[Middle] > Target:
            UB = Middle - 1
        elif Array[Middle] < Target:
            LB = Middle + 1
        else:
            return Middle
    return -1                

Array = [100,200,300,400,500,600,700,800,900,1000]
LB = 0
UB = len(Array)-1
Target = 700

A = Binary_Search(Array, LB , UB , Target)
if A != -1:
    print(Target, "is at indext" , A)
else:
    print(Target, "is not found in the Array.")