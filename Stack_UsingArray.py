'''Implement a stack using an array'''
class Stack:
    
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0
    # push - adds an item to the top of the stack
    def push(self, data):
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()
        
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1
    # pop - removes an item from the top of the stack (and returns the value of that item)
    def pop(self):
        # Check if the stack is empty and, if it is, return None
        if self.is_empty():
            self.next_index = 0
            return None
        # Decrement next_index and num_elements
        self.next_index -= 1
        self.num_elements -= 1
        # Return the item that is being "popped"
        return self.arr[self.next_index]
    # size - returns the size of the stack
    def size(self):
        return self.num_elements
    # is_empty - returns True if the stack is empty and False otherwise
    def is_empty(self):
        return self.num_elements == 0
    # Method to avoid a stack overflow
    def _handle_stack_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for _ in range( 2* len(old_arr))]
        for index, value in enumerate(old_arr):
            self.arr[index] = value
