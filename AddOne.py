'''You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

Example 1:

input = [1, 2, 3]
output = [1, 2, 4]
Example 2:

input = [1, 2, 9]
output = [1, 3, 0]
Example 3:

input = [9, 9, 9]
output = [1, 0, 0, 0]
Challenge: One way to solve this problem is to convert the input array into a number and then add one to it. For example, if we have input = [1, 2, 3], you could solve this problem by creating the number 123 and then separating the digits of the output number 124.

But can you solve it in some other way?'''
def add_one(arr):
    carry = 1
    new_arr = []
    # Traverse the array in reverse
    for i in range(len(arr)-1,-1, -1):
        digit = carry + arr[i]
        if digit != 10:
            carry = 0
            new_arr.append(digit)
        else:
            new_arr.append(0)
    if carry == 1:
        new_arr.append(1)
    return new_arr[::-1]
# Testing  
# arr=[9,9,9]
# print(add_one(arr)) #This will print [1,0,0,0]
