'''Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.

For exmaple, if n = 4, then output = [1, 4, 6, 4, 1].

To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html'''
def nth_row_pascal(n):
    if n == 0:
        return [1]
    current_row = [1] #First row
    for i in range(1, n+1): #i denotes the row number
        previous_row = current_row #set the 'current_row' from previous iteration as 'previous_row'
        current_row = [1] # add the default first element
        for j in range(1,i):
            # An element at position `j` in the current row is the 
            # sum of elements at position `j` and `j-1` in the previous row.
            next_num = previous_row[j] + previous_row[j-1]
            current_row.append(next_num)
        current_row.append(1) #append the default last element
    return current_row
#Test Cases
# n = 4
# print(nth_row_pascal(n)) #[1, 4, 6, 4, 1]
