'''Implement a stack using a linked list'''
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.head = None # No items in the stack, so head should be None
        self.num_elements = 0 # No items in the stack, so num_elements should be 0
    
    def push(self, value): # adds an item to the top of the stack
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head # place the new node at the head (top) of the linked list
            self.head = new_node

        self.num_elements += 1
    
    def size(self): # returns the current size of the stack
        return self.num_elements
    
    def is_empty(self): # returns True if the stack is empty and False otherwise
        return self.num_elements == 0
    
    def pop(self): # removes an item from the top of the stack (and returns the value of that item)
        if self.is_empty():
            return None

        value = self.head.value # copy data to a local variable
        self.head = self.head.next # move head pointer to point to next node (top is removed by doing so)
        self.num_elements -= 1
        return value
# # Test Cases
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.push(40)
# stack.push(50)

# # Test size
# print ("Pass" if (stack.size() == 5) else "Fail")

# # Test pop
# print ("Pass" if (stack.pop() == 50) else "Fail")

# # Test push
# stack.push(60)
# print ("Pass" if (stack.pop() == 60) else "Fail")
# print ("Pass" if (stack.pop() == 40) else "Fail")
# print ("Pass" if (stack.pop() == 30) else "Fail")
# stack.push(50)
# print ("Pass" if (stack.size() == 3) else "Fail")
'''Time complexity of stacks using linked lists
Notice that if we pop or push an element with this stack, there's no traversal. We simply add or remove the item from the head of the linked list, and update the head reference. So with our linked list implementaion, pop and push have a time complexity of O(1).

Also notice that using a linked list avoids the issue we ran into when we implemented our stack using an array. In that case, adding an item to the stack was fine—until we ran out of space. Then we would have to create an entirely new (larger) array and copy over all of the references from the old array.

That happened because, with an array, we had to specify some initial size (in other words, we had to set aside a contiguous block of memory in advance). But with a linked list, the nodes do not need to be contiguous. They can be scattered in different locations of memory, an that works just fine. This means that with a linked list, we can simply append as many nodes as we like. Using that as the underlying data structure for our stack means that we never run out of capacity, so pushing and popping items will always have a time complexity of O(1).'''
