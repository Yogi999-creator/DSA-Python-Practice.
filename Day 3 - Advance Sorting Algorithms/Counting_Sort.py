# Counting Sort Algorithm Implementation in Python.
# @code by: Mundhra Yogesh Pawan.

def Counting_Sort(Array):
    size = len(Array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        count[Array[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[Array[i]] - 1] = Array[i]
        count[Array[i]] -= 1
        i -= 1

    for i in range(0, size):
        Array[i] = output[i]

Array = [4, 2, 2, 8, 3, 3, 1]
Counting_Sort(Array)
print("Sorted Array:",Array)