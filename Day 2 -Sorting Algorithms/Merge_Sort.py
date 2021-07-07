# Merge Sort Algorithm Implementation in Python.
# @code by: Mundhra Yogesh Pawan.

def Merge_Sort(Array):

    if len(Array) > 1:
         Middle = len(Array) // 2
         Left_Array = Array[:Middle]
         Right_Array = Array[Middle:]
         Merge_Sort(Left_Array)
         Merge_Sort(Right_Array) 

         i = 0
         j = 0
         k = 0

         while i < len(Left_Array) and j < len(Right_Array):
             if Left_Array[i] < Right_Array[j]:
                Array[k] = Left_Array[i] 
                i += 1
                k += 1 
             else:
                Array[k] = Right_Array[j]
                j += 1
                k += 1

         while i < len(Left_Array):
             Array[k] = Left_Array[i]
             i += 1
             k += 1

         while j < len(Right_Array):
             Array[k] = Right_Array[j]
             j += 1
             k += 1           

number = int(input("How many elements in the array: "))
Array = [int(input()) for i in range(number)]
Merge_Sort(Array)
print("Sorted Array: ",Array)



