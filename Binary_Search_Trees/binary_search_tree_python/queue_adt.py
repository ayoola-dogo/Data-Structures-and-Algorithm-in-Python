# FIFO First In First Out Structure

class Queue:

    def __init__(self):
        self.queue = []

    # O(1) constant running time complexity
    def is_empty(self):
        return self.queue == []

    # This operation has a O(1) constant running time complexity
    def enqueue(self, data):
        self.queue.append(data)

    # This operation has a O(N) linear running time complexity
    def dequeue(self):
        if not self.is_empty():
            item = self.queue[0]   # O(1) constant time complexity
            del self.queue[0]   # O(N) linear time complexity
            return item
        else:
            return ":queue is empty"

    # This operation has a O(1) constant running time complexity
    def peek(self):
        item = self.queue[0]
        return item

    # This operation has a O(1) constant running time complexity
    def size_queue(self):
        length = self.queue.__len__()
        return length
