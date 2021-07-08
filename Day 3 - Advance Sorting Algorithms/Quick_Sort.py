# Quick Sort Algorithm Implementation in Python.
# @code by: Mundhra Yogesh Pawan.

def Partition(Array, low, high):
  pivot = Array[high]
  i = low - 1

  for j in range(low, high):
    if Array[j] <= pivot:
      i = i + 1
      (Array[i], Array[j]) = (Array[j], Array[i])

  (Array[i + 1], Array[high]) = (Array[high], Array[i + 1])

  return i + 1

def Quick_Sort(Array, low, high):
  if low < high:
    p = Partition(Array, low, high)
    Quick_Sort(Array, low, p - 1)
    Quick_Sort(Array, p + 1, high)

Array = [8, 7, 2, 1, 0, 9, 6]
Quick_Sort(Array, 0, len(Array) - 1)
print("Sorted Array:",Array)