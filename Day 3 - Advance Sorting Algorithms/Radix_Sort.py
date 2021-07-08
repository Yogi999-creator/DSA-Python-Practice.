# Radix Sort Algorithm Implementation in Python.
# @code by: Mundhra Yogesh Pawan.

def Counting_Sort(Array, place):
    size = len(Array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = Array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = Array[i] // place
        output[count[index % 10] - 1] = Array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        Array[i] = output[i]

def Radix_Sort(Array):
    max_element = max(Array)
    place = 1
    while max_element // place > 0:
        Counting_Sort(Array, place)
        place *= 10

Array = [121, 432, 564, 23, 1, 45, 788]
Radix_Sort(Array)
print("Sorted Array:",Array)