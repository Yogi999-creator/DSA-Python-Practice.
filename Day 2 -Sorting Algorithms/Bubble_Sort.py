# Bubble Sort Algorithm Implementation in Python.
# @code by: Mundhra Yogesh Pawan.

def Bubble_Sort(Array):
    N = len(Array)
    for i in range(N-1):
        flag = 0
        for j in range(N-1-i):
            if Array[j] > Array[j+1]:
                temp = Array[j]
                Array[j] = Array[j+1]
                Array[j+1] = temp
                flag = 1
        if flag == 0:
            break
    return Array

Array = [100,20,30,50,70,90,40,10,60,80]                 
A = Bubble_Sort(Array)
print("Sorted Array:", A)