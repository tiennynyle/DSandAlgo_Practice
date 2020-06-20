'''You are given the head of a linked list and two integers, i and j. You have to retain the first i nodes and then delete the next j nodes.
 Continue doing so until the end of the linked list.

Example:

linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
i = 2
j = 3
Output = 1 2 6 7 11 12'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def skip_i_delete_j(head, i, j):
    p1 = head
    p2 = None
    
    if head is None or i<0 or j<0: #Invalid input
        return head
    if i == 0: #Skip 0 nodes meaning Delete all
        return None
    if j == 0: #Delete 0 nodes
        return head
    while p1:
        #Skip i - Move p1 to position i-1:
        for _ in range (0,i-1):
            if p1 is None:
                break
            p1 = p1.next
        if not p1:
            return head
        #Assign p2 to position i(first node to delete)
        p2 = p1.next
        #Move p2 to the last node to delete
        for _ in range (0,j-1):
            if p2 is None:
                break
            p2 = p2.next
        #Delete the j nodes by referencing p1 to the node next to p2
        if not p2: 
            p1.next = None
        else:
            p1.next = p2.next 
            p2.next = None
        p1 = p1.next
    return head
# # Helper functions and Test Cases for testing purpose
# def create_linked_list(arr):
#     if len(arr)==0:
#         return None
#     head = Node(arr[0])
#     tail = head
#     for data in arr[1:]:
#         tail.next = Node(data)
#         tail = tail.next
#     return head

# def print_linked_list(head):
#     while head:
#         print(head.data, end=' ')
#         head = head.next
#     print()
# def test_function(test_case):
#     head = test_case[0]
#     i = test_case[1]
#     j = test_case[2]
#     solution = test_case[3]
        
#     temp = skip_i_delete_j(head, i, j)
#     index = 0
#     try:
#         while temp is not None:
#             if temp.data != solution[index]:
#                 print("Fail")
#                 return
#             index += 1
#             temp = temp.next
#         print("Pass")
#     except Exception as e:
#         print("Fail")
# arr = [1, 2, 3, 4, 5]
# i = 2
# j = 0
# head = create_linked_list(arr)
# solution = [1, 2, 3, 4, 5]
# test_case = [head, i, j, solution]
# test_function(test_case)
# arr = [1, 2, 3, 4, 5]
# i = 2
# j = 4
# head = create_linked_list(arr)
# solution = [1, 2]
# test_case = [head, i, j, solution]
# test_function(test_case)
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# i = 2
# j = 3
# head = create_linked_list(arr)
# solution = [1, 2, 6, 7, 11, 12]
# test_case = [head, i, j, solution]
# test_function(test_case)
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# i = 2
# j = 2
# head = create_linked_list(arr)
# solution = [1, 2, 5, 6, 9, 10]
# test_case = [head, i, j, solution]
# test_function(test_case)
