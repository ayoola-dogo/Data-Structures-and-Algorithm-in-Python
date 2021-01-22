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


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print("Dequeue {}".format(queue.dequeue()))
print("Size of queue {}".format(queue.size_queue()))
print("---------------------------------------------")
print("Dequeue {}".format(queue.dequeue()))
print("Size of queue {}".format(queue.size_queue()))
print("---------------------------------------------")
print("Dequeue {}".format(queue.dequeue()))
print("Size of queue {}".format(queue.size_queue()))
print("---------------------------------------------")
print("Dequeue {}".format(queue.dequeue()))
print("Size of queue {}".format(queue.size_queue()))
print("---------------------------------------------")
print("Dequeue {}".format(queue.dequeue()))
print("Size of queue {}".format(queue.size_queue()))
