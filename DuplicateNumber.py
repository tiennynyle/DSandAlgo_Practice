'''You have been given an array of length = n. The array contains integers from
 0 to n - 2. Each number in the array is present exactly once except for one number
  which is present twice. Find and return this duplicate number present in the array

Example:
arr = [0, 2, 3, 1, 4, 5, 3]
output = 3 (because 3 is present twice)

The expected time complexity for this problem is O(n) and the expected space-complexity
is O(1).'''

def duplicate_number(arr):
    expected_sum = 0
    current_sum = 0
    for i in range(len(arr)-1):
        expected_sum += i
    for num in arr:
        current_sum += num
    return (current_sum - expected_sum)
# # Test
# arr=[0, 2, 3, 1, 4, 5, 3]
# print(duplicate_number(arr))
