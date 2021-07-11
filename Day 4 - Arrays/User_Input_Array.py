# Array (User Input) Implementation in Python.
# @code by: Mundhra Yogesh Pawan.

Array = []
Size = int(input("Size of Array: "))
i = 0
while (i < Size):
    Array.append(int(input("Enter elements in the Array: ")))
    i += 1
i = 0
while (i < len(Array)):
    Array[i]
    i += 1 
print("Array:",Array)