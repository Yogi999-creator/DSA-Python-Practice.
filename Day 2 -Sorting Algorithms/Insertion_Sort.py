# Insertion Sort Algorithm Implementation in Python.
# @code by: Mundhra Yogesh Pawan.

def insertion_sort(Array):
    
    for i in range(1, len(Array)):
        current_element = Array[i]
 
        while Array[i-1] > current_element and i > 0:
            Array[i], Array[i-1] = Array[i-1], Array[i]
            i = i - 1
    return Array
 
A = [4,6,8,3,2,5,1,7,9,0]
print("Sorted Array: ",insertion_sort(A))