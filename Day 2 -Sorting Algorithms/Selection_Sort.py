# Selection Sort Algorithm Implementation in Python.
# @code by: Mundhra Yogesh Pawan.

def Selection_Sort(Array):
    n = len(Array)

    for i in range(0,n-1):
        minValueIndex = i

        for j in range(i+1, n):
            if Array[j] < Array[minValueIndex]:
                minValueIndex = j

        if minValueIndex !=i:
            temp = Array[i]
            Array[i] = Array[minValueIndex]
            Array[minValueIndex] = temp

    return Array

Array = [21,6,9,33,3]
print(Selection_Sort(Array))