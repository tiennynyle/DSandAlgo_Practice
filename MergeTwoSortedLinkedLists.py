# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones. 
# User defined class
class Node:
    def __init__(self, value): # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
# User defined class
class LinkedList: 
    def __init__(self, head): # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head
    
    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''
    def append(self, value):
        
        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return
        
        # Create a temporary Node object
        node = self.head
        
        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next
        
        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)

        
    '''We will need this function to convert a LinkedList object into a Python list of integers'''
    def to_list(self):
        out = []          # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object
        
        while node:       # <-- Iterate untill we have nodes available
            out.append(int(str(node.value))) # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next
        
        return out
def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    '''
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    '''
    # if list1 is empty, return list2 and vice versa
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    # if neither are empty
    tmp = dummy = LinkedList(Node(0))
    p1 = list1.head
    p2 = list2.head
    while p1 and p2:
        if p1.value <= p2.value:
            tmp.next = p1
            p1 = p1.next
            tmp = tmp.next
        else:
            tmp.next = p2
            p2 = p2.next
            tmp = tmp.next
    if p1 is None:
        tmp.next = p2
    if p2 is None:
        tmp.next = p1
    ll = LinkedList(dummy.next)
    return ll
# # We can use the append function in helper code:
# def merge(list1, list2):
#     # if list1 is empty, return list2 and vice versa
#     if list1 is None:
#         return list2
#     if list2 is None:
#         return list1
#     # if neither are empty
#     merged = LinkedList(None)
#     p1 = list1.head
#     p2 = list2.head
#     while p1 and p2:
#         if p1.value <= p2.value:
#             merged.append(p1)
#             p1 = p1.next
#         else:
#             merged.append(p2)
#             p2 = p2.next
#     if p1 is None:
#         merged.append(p2)
#     if p2 is None:
#         merged.append(p1)
#     return merged

# # Test merge() function
# linked_list = LinkedList(Node(1))
# linked_list.append(3)
# linked_list.append(5)

# second_linked_list = LinkedList(Node(2))
# second_linked_list.append(4)

# merged = merge(linked_list, second_linked_list)
# node = merged.head
# while node is not None:
#     #This will print 1 2 3 4 5
#     print(node.value)
#     node = node.next
    
# # Lets make sure it works with a None list
# merged = merge(None, linked_list)
# node = merged.head
# while node is not None:
#     #This will print 1 3 5
#     print(node.value)
#     node = node.next
