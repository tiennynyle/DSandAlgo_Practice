class Queue():
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range (initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0
    def handle_full_capacity(self):
        old_arr = self.arr # Define an old_arr variable and assign the the current (full) array so that we have a copy of it
        self.arr = [0 for _ in range (2 * len(old_arr))] # Create a new (larger) array and assign it to arr

        index = 0

        # copy all elements from front of queue (front-index) until end
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

        # case: when front-index is ahead of next index
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        # reset pointers
        self.front_index = 0
        self.next_index = index

    def enqueue(self,value):
        if self.queue_size == len(self.arr):
            self.handle_full_capacity()
        
        self.arr[self.next_index] = value # Take a value as input and assign this value to the next free slot in the array
        self.queue_size += 1 # Increment queue_size
        self.next_index = (self.next_index + 1) % len(self.arr) # Increment next_index
        if self.front_index == -1: # If the front index is -1 (because the queue was empty), it should set the front index to 0
            self.front_index = 0

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0
    
    def front(self):
        # check if queue is empty
        if self.is_empty():
            return None
        return self.arr[self.front_index]

    def dequeue(self):
        # check if queue is empty
        if self.is_empty():
            self.front_index = -1   # resetting pointers
            self.next_index = 0
            return None

        # dequeue front element
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value
    
# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")
