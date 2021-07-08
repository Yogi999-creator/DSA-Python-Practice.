# Bucket Sort Algorithm Implementation in Python.
# @code by: Mundhra Yogesh Pawan.

def Bucket_Sort(Array):
    Bucket = []

    for i in range(len(Array)):
        Bucket.append([])

    for j in Array:
        index = int(10 * j)
        Bucket[index].append(j)

    for i in range(len(Array)):
        Bucket[i] = sorted(Bucket[i])

    k = 0
    for i in range(len(Array)):
        for j in range(len(Bucket[i])):
            Array[k] = Bucket[i][j]
            k += 1
    return Array

Array = [.42, .32, .33, .52, .37, .47, .51]
print("Sorted Array:",Bucket_Sort(Array))