"""
Question - Let's use recursion to help us solve the following permutation problem:

Given a list of items, the goal is to find all of the permutations of that list. For example,
Given a list like: [0, 1, 2]
Permutations: [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

Notice that the expected output is a list of permutation with each permuted item being represented by a list. Such an object that contains other object is called "compound" object.

The Idea
Build a compoundList incrementally starting with a blank list, and permute (add) each element of original input list at all possible positions.


For example, take [0, 1, 2] as the original input list:

Start with a blank compoundList [[]]. This is actually the last call of recursive function stack. Pick the element 2 of original input list, making the compoundList as [[2]]


Pick next element 1 of original input list, and add this element at position 0, and 1 for each list of previous compoundList. We will require to create copy of all lists of previous compoundList, and add the new element. Now, the compoundList will become [[1, 2], [2, 1]].


Pick next element 0 of original input list, and add this element at position 0, 1, and 2 for each list of previous compoundList. Now, the compoundList will become [[0, 1, 2], [1, 0, 2], [1, 2, 0], [0, 2, 1], [2, 0, 1], [2, 1, 0]] .

Additional Resource:
While dealing with a "compound" object, a simple copy operation might not work as expected. You would need a function that can create a deep copy. For this purpose, you can make use of deepcopy() function from the copy module in Python. This module provides the function for normal (Shallow) and deep copy operations
"""
import copy                                # We will use `deepcopy()` function from the `copy` module

def permute(inputList):
    result = []
    # Base case:
    if len(inputList) == 0:
        result.append([])
    else:
        first_element = inputList[0]
        perms = permute(inputList[1:])
        for perm in perms:
            for i in range(0,len(perm) + 1):
                copied_perm = copy.deepcopy(perm)
                copied_perm.insert(i, first_element)
                result.append(copied_perm)
    return result
# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.
    
    Note that the ordering of the list is not important.
    
    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list
    
    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input
    
    o.sort()
    e.sort()
    return o == e
# Test Cases 
print ("Pass" if  (check_output(permute([]), [[]])) else "Fail")
print ("Pass" if  (check_output(permute([0]), [[0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")
