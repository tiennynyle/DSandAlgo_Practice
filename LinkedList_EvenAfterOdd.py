'''Given a linked list with integer data, arrange the elements in such a manner that
all nodes with even numbers are placed after odd numbers. Do not create any new nodes
and avoid using any other data structure. The relative order of even and odd elements
must not change.

Example:

linked list = 1 2 3 4 5 6
output = 1 3 5 2 4 6'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    even_tail = None
    even_head = None
    odd_tail = None
    odd_head = None
    tmp = None
    while head:
        tmp = head.next
        head.next = None
        if head.data % 2 == 0:
            add_node(head, even_head, even_tail)
        else:
            add_node(head,odd_head, odd_tail)
        head = tmp
    if odd_tail is None:
        head = even_head
    else:
        head = odd_head
        odd_tail.next = even_head
    return head
def add_node(node_to_add, head_ptr, tail_ptr):
    if head_ptr is None:
        head_ptr = node_to_add
        tail_ptr = node_to_add
        return head_ptr
    tail_ptr.next = node_to_add
    tail_ptr = node_to_add
    return head_ptr
# #Helper functions for testing and test cases
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
#     solution = test_case[1]
    
#     node_tracker = dict({})
#     node_tracker['nodes'] = list()
#     temp = head
#     while temp:
#         node_tracker['nodes'].append(temp)
#         temp = temp.next

#     head = even_after_odd(head)    
#     temp = head
#     index = 0
#     try:
#         while temp:
#             if temp.data != solution[index] or temp not in node_tracker['nodes']:
#                 print("Fail")
#                 return
#             temp = temp.next
#             index += 1
#         print("Pass")            
#     except Exception as e:
#         print("Fail")
# arr = [1, 2, 3, 4, 5, 6]
# solution = [1, 3, 5, 2, 4, 6]

# head = create_linked_list(arr)
# test_case = [head, solution]
# test_function(test_case)
# arr = [1, 3, 5, 7]
# solution = [1, 3, 5, 7]

# head = create_linked_list(arr)
# test_case = [head, solution]
# test_function(test_case)

# arr = [2, 4, 6, 8]
# solution = [2, 4, 6, 8]
# head = create_linked_list(arr)
# test_case = [head, solution]
# test_function(test_case)
