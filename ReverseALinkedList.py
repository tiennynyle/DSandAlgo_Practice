# Helper Code

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])

def reverse(linked_list):
    """
        Reverse the inputted linked list

        Args:
        linked_list(obj): Linked List to be reversed
        Returns:
        obj: Reveresed Linked List
        """
    #if linked list is empty
    if linked_list.head is None: 
        return None
    #if linked list has only 1 node
    elif linked_list.head.next is None: 
        return linked_list
    #if linked list has more than 1 node
    p = linked_list.head #create a pointer to head
    prev = None 
    tmp = p.next 
    while tmp:
        p.next = prev
        prev = p
        p = tmp
        tmp = p.next
    #the last node is being left out after the while loop
    p.next = prev #referencing the last node to the previous one
    linked_list.head = p


#Test
llist = LinkedList()
for value in [0,1,2,3,4]:
    llist.append(value)

flipped = reverse(llist)
print(llist)

