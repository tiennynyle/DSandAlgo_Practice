class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """
    # return False if list is empty
    if linked_list is None:
        return False
    
    fast_p = linked_list.head
    slow_p = linked_list.head
    # execute the loop until we get to a node where fast_p or its next node doesn't exist 
    while fast_p and fast_p.next:
        slow_p = slow_p.next      # slow pointer moves one node
        fast_p = fast_p.next.next # fast pointer moves two nodes
        # if the two nodes meet, the linked list has loop
        if slow_p == fast_p:
            return True
    return False

## Testing
#list_with_loop = LinkedList([2, -1, 3, 0, 5])

## Creating a loop where the last node points back to the second node
# loop_start = list_with_loop.head.next

# node = list_with_loop.head
# while node.next: 
#     node = node.next   
# node.next = loop_start   
## Create another circular linked list
# small_loop = LinkedList([0])
# small_loop.head.next = small_loop.head

# print ("Pass" if iscircular(list_with_loop) else "Fail")                  # Pass
# print ("Pass" if iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")   # Fail
# print ("Pass" if iscircular(LinkedList([1])) else "Fail")                 # Fail
# print ("Pass" if iscircular(small_loop) else "Fail")                      # Pass
# print ("Pass" if iscircular(LinkedList([])) else "Fail")                  # Fail
