class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()
# # Testing
# MyStack = Stack()

# MyStack.push("Web Page 1")
# MyStack.push("Web Page 2")
# MyStack.push("Web Page 3")
# MyStack.pop()

# print (MyStack.items)
