class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        # TODO: Write function to prepend here
        if self.head is None:
            self.head = Node(value)
            return
        tmp = self.head
        self.head = Node(value)
        self.head.next = tmp
        return

# LinkedList.prepend = prepend
    def append(self, value):
        """ Append a value to the end of the list. """            
        if self.head is None:
            node = Node(value)
            self.head = node
            self.tail = node
            return
        node = Node(value)
        self.tail.next = node
        self.tail = node
        return

    def search(self,value):
        if self.head is None:
            return None
        p = self.head
        while p:
            if p.value == value:
                return p
            p = p.next

    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is None:
            return None
        if self.head.value == value:
            tmp = self.head.next
            self.head = tmp
            return
        p = self.head.next
        prev = self.head
        while p:
            if p.value == value:
                tmp = p.next #tmp = 3
                prev.next = tmp #prev ->3
                return
            else:
                prev = p
                p = p.next 
    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            return None
        else:
            tmp = self.head.value
            self.head = self.head.next
            return tmp
    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """
        count = 0
        if count == pos:
            node = Node(value)
            tmp = self.head
            self.head = node
            self.head.next = tmp
            return
        p = self.head
        while p.next is not None:
            if count == pos -1 :
                # Create a node
                node = Node(value)
                # Keep reference to the next p 
                tmp = p.next
                # make p pointer link to node 
                p.next = node
                # make node link to tmp
                node.next = tmp
                return 
            p = p.next
            count += 1
        
        # After finishing the loop, and we are not count == pos -1
        if count <= pos -1:
            # Create new node 
            node = Node(value)
            # Make p ( which is the tail node , end of the list) links to new node
            p.next = node
        return self.head
    def size(self):
        """ Return the size or length of the linked list. """
        if self.head is None:
            return 0
        count = 0
        p = self.head
        while p:
            count += 1
            p = p.next
        return count 
#Test size function
linked_list = LinkedList()
linked_list.append(0)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.size()
print(linked_list.size())
