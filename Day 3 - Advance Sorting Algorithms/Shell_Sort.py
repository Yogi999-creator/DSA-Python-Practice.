# Shell Sort Algorithm Implementation in Python.
# @code by: Mundhra Yogesh Pawan.

def Shell_Sort(Array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = Array[i]
            j = i
            while j >= interval and Array[j - interval] > temp:
                Array[j] = Array[j - interval]
                j -= interval
            Array[j] = temp
        interval //= 2

Array = [9, 8, 3, 7, 5,2, 6, 4, 1]
size = len(Array)
Shell_Sort(Array, size)
print('Sorted Array:', Array)