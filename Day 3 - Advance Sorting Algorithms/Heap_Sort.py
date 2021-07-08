# Heap Sort Algorithm Implementation in Python.
# @code by: Mundhra Yogesh Pawan.

def Heapify(Array, n, i):
    largest = i    
    l = 2 * i + 1
    r = 2 * i + 2
        
    if l < n and Array[i] < Array[l]:
        largest = l
        
    if r < n and Array[largest] < Array[r]:
        largest = r
 
    if largest != i:
        Array[i], Array[largest] = Array[largest], Array[i]
        Heapify(Array, n, largest)
  
def Heap_Sort(Array):
    n = len(Array)

    for i in range(n//2, -1, -1):
        Heapify(Array, n, i)
  
    for i in range(n-1, 0, -1):
        Array[i], Array[0] = Array[0], Array[i]
        Heapify(Array, i, 0)
  
Array = [1, 12, 9, 5, 6, 10]
Heap_Sort(Array)
n = len(Array)
print("Sorted Array:", Array)