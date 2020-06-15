'''Suppose you have a linked list where the value of each node is a sorted linked list
 (i.e., it is a nested list). Your task is to flatten this nested list—that is, to 
 combine all nested lists into a single (sorted) linked list.'''
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
    # if list1 is empty, return list2 and vice versa
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    # if neither are empty
    merged = LinkedList(None)
    p1 = list1.head
    p2 = list2.head
    while p1 and p2:
        if p1.value <= p2.value:
            merged.append(p1)
            p1 = p1.next
        else:
            merged.append(p2)
            p2 = p2.next
    if p1 is None:
        merged.append(p2)
    if p2 is None:
        merged.append(p1)
    return merged

''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''
class NestedLinkedList(LinkedList):
    # Iterative Solution 
    def _flatten(self, node):
        if node is None:
            return None 
        if node.next is None:
            # Value is linnked list 
            return node.value
        tmp_list = node.value
        curr = node.next
        while curr is not None:
            tmp_list = merge(tmp_list, curr.value)
            curr = curr.next
        return tmp_list

    #Recursive Solution
    def flatten_recursive (self):
        return self.flatten_res(self.head)
    def flatten_res(self, node):
        if node.next is None:
            return node.value 
        return merge(node.value, self.flatten_res(node.next))


# # Test merge() function
# linked_list = LinkedList(Node(1))
# linked_list.append(3)
# linked_list.append(5)

# second_linked_list = LinkedList(Node(2))
# second_linked_list.append(4)

# nested_linked_list = NestedLinkedList(Node(linked_list)) # <-- Notice that we are passing a Node made up of a simple LinkedList object
# nested_linked_list.append(second_linked_list)

# #Test flattening functions
#print (nested_linked_list.flatten_recursive().to_list()) #Print [1,2,3,4,5]
#print (nested_linked_list._flatten(nested_linked_list.head).to_list()) #Print [1,2,3,4,5]
