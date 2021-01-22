# LIFO: Last In First Out Structure

class Stack:

    def __init__(self):
        self.stack = []  # Stack is going to be a one-dimensional array

    # insert item into the stack
    # This operation has O(1) running time complexity
    def push(self, data):
        self.stack.append(data)

    # Remove and Return the last item we have inserted (LIFO)
    # This operation has O(1) running time complexity
    def pop(self):
        if not self.is_empty():
            # item = self.stack.pop() OR
            item = self.stack[-1]  # O(1) time complexity
            del self.stack[-1]  # O(1) time complexity
            return item
        else:
            return -1

    # Returns the last item but does not remove it from the array
    # Has O(1) running time complexity
    def peek(self):
        item = self.stack[-1]
        return item

    # This operation has a O(1) running time complexity
    def is_empty(self):
        if not self.stack:
            return True

    # This operation has a O(1) running time complexity
    def stack_size(self):
        length = self.stack.__len__()
        return length
