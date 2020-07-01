def add_one(arr):
    #Base case
    if arr == [9]:
        return [1,0]
    # A simple case, where we just need to increment the last digit
    if arr[-1] < 9:
        arr[-1] += 1
    # We have used arr[:-1], that means all elements of the list except the last one.
    # Example, for original input arr=[1,2,9], we will pass [1,2] in next call.
    else:
        arr = add_one(arr[:-1]) + [0]
    return arr
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass") 
# Test Case 1    
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)
# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)
# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)
