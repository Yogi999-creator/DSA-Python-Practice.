# Write a program to reverse an array or string. (Python Implementation)
# @code by: Mundhra Yogesh Pawan.

# Method-1.
'''
def Reverse_Array(Array, Start, End):
    while Start < End:
        Array[Start] , Array[End] = Array[End] , Array[Start]
        Start += 1
        End -= 1
    
Array = [1,2,3,4,5]
print("Given Array:", Array)
Reverse_Array(Array,0,4)
print("Reversed Array:", Array)
'''


# Method-2.
''''
Array = ["Hello", "Ji", "Yogesh", "Pawan", "Mundhra"]
print("Given Array:", Array)
ReverseArray = Array[::-1]
print("Reversed Array:", ReverseArray)
'''