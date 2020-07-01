def permutations(string):
    if len(string) == 1:
        return(string)
    
    result = []
    perms = permutations(string[1:])
    current_char = string[0]
    # Iterate over each perm available in the list returned from previous call
    for perm in perms:
        # place the current character at different indices of the sub-string
        for i in range (len(perm)+1):
            result.append(perm[:i] + current_char + perm[i:])
    
    return result

def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")
# Test Cases
string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)
string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)
string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)
'''Credit to https://www.youtube.com/watch?v=4lIQCoG4MnY'''
