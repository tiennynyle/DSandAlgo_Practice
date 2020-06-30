def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
# Test Cases
print ("Pass" if (1 == factorial(0)) else "Fail")
print ("Pass" if  (1 == factorial(1)) else "Fail")
print ("Pass" if  (120 == factorial(5)) else "Fail")
