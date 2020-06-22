'''Given a linked list, swap the two nodes present at position i and j, assuming 0 <= i <= j. 
The positions are based on 0-based indexing.

Note: You have to swap the nodes and not just the values.

Example:

linked_list = 3 4 5 2 6 1 9
positions = 2 5
output = 3 4 1 2 6 5 9'''
class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None
"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped

TODO: complete this function and swap nodes present at position_one and position_two
Do not create a new linked list
"""
def swap_nodes(head, position_one, position_two):

    curr1, prev2, curr2 = None, None, None
    current_index = 0
    current_node = head

    # Making a dummy node in case we need to change the head
    # For example, 4 -> 5 -> 6 -> 8
    # After having dummynode, -1 -> 4 -> 5 -> 6 -> 8
    dummy_node = Node(-1)
    dummy_node.next = head
    prev1 = dummy_node
    
    # Special Case, when we need to swap an element in the first position 
    # curr1 will point to current_node 
    if position_one - 1 == -1:
        curr1 = current_node

    if position_one == position_two:
        return head
    
    while current_node :
        if current_index == position_one - 1:
            prev1 = current_node
            curr1 = current_node.next
        elif current_index == position_two-1:
            prev2 = current_node
            curr2 = current_node.next
            # Stop until when we have the position for the second node
            break
        
        current_node = current_node.next
        current_index +=1
    
    tmp = curr1.next
    prev1.next = curr2
    curr1.next = curr2.next 

    # If two nodes that are needed to swap is consecutive. 
    if curr1 == prev2:
        curr2.next = curr1    
    else:
        curr2.next = tmp
        prev2.next = curr1

    # Returning whatever next of dummy which is a head
    return dummy_node.next

# # Helper functions for testing and test cases 
# def test_function(test_case):
#     head = test_case[0]
#     left_index = test_case[1]
#     right_index = test_case[2]
    
#     left_node = None
#     right_node = None
    
#     temp = head
#     index = 0
#     try:
#         while temp is not None:
#             if index == left_index:
#                 left_node = temp
#             if index == right_index:
#                 right_node = temp
#                 break
#             index += 1
#             temp = temp.next
#         updated_head = swap_nodes(head, left_index, right_index)
#         temp = updated_head
#         index = 0
#         pass_status = [False, False]

#         while temp is not None:
#             if index == left_index:
#                 pass_status[0] = temp is right_node
#             if index == right_index:
#                 pass_status[1] = temp is left_node

#             index += 1
#             temp = temp.next

#         if pass_status[0] and pass_status[1]:
#             print("Pass")
#         else:
#             print("Fail")
#         return updated_head
#     except Exception as e:
#         print (e)
#         print("Fail")
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
#         print(head.data, end=" ")
#         head = head.next
#     print()

# arr = [3, 4, 5, 2, 6, 1, 9]
# left_index = 0
# right_index = 1
# head = create_linked_list(arr)
# test_case = [head, left_index, right_index]
# updated_head = test_function(test_case)

# arr = [3, 4, 5, 2, 6, 1, 9]
# left_index = 2 
# right_index = 4
# head = create_linked_list(arr)
# test_case = [head, left_index, right_index]
# updated_head = test_function(test_case)



