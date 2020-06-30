def is_palindrome(input):
    if len(input) == 0 or len(input) == 1:
        return True
    else:
        return input[0] == input[-1] and is_palindrome(input[1:-1])
#Test Cases
print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")
