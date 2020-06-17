'''You have been given an array containing numbers. Find and return the largest 
sum in a contiguous subarray within the input array.

Example 1:

arr= [1, 2, 3, -4, 6]
The largest sum is 8, which is the sum of all elements of the array.
Example 2:

arr = [1, 2, -5, -4, 1, 6]
The largest sum is 7, which is the sum of the last two elements of the array.'''
def max_sum_subarray(arr):
    current_max = arr[0] #largest sum of subarray till the current index
    global_max = arr[0] #largest sum of subarray 
    #loop through the array starting at position 1
    for num in arr[1:]:
        #update current_max to the higher value between the current_max + num and num
        current_max = max(current_max + num, num)
        #update the global max to the higher value between the new current_max and the current global_max
        global_max = max(current_max, global_max)
    return global_max

# Test cases
# arr= [1, 2, 3, -4, 6] #8
# arr = [1, 2, -5, -4, 1, 6] #7
# arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4] #18
# print(max_sum_subarray(arr))
'''Credit to: https://www.youtube.com/watch?v=86CQq3pKSUw for explaining how Kadane's Algorithm works '''
