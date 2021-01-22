class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        try:
            return "pre({0})||data({1})||next({2})".format(self.previous.data, self.data, self.next.data)
        except AttributeError:
            if self.previous is None:
                return "pre(None)||data({0})||next({1})".format(self.data, self.next.data)
            elif self.next is None:
                return "pre({0})||data({1})||next(None)".format(self.previous.data, self.data)
            else:
                return "pre(None)||data({})||next(None)".format(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.root = None
        self.num_of_nodes = 0

    @staticmethod
    def create_node(data):
        node = Node(data)
        return node

    # O(N) linear running time complexity
    def traverse(self):
        actual_node = self.root

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next

    # This has a O(N) linear running time complexity
    def search(self, data):
        actual_node = self.root

        while actual_node is not None and actual_node.data != data:
            actual_node = actual_node.next
        if actual_node is None:
            print("data not found")
        else:
            print("node:", actual_node)
            return actual_node

    # This has a O(1) constant running time complexity
    def insert_start(self, data):
        node = self.create_node(data)
        if self.root is None:
            self.root = node
        else:
            node.next = self.root
            self.root.previous = node
            self.root = node
        self.num_of_nodes += 1

    # This is a O(N) running time complexity
    def insert_end(self, data):
        node = self.create_node(data)

        actual_node = self.root

        while actual_node.next is not None:
            actual_node = actual_node.next
        node.previous = actual_node
        actual_node.next = node
        self.num_of_nodes += 1

    # Using the search method to return a particular node based on the data supplied.
    # The big O notation of removing the said node is O(1) constant running time complexity.
    def remove(self, node):
        try:
            node.previous.next = node.next
            node.next.previous = node.previous
        except AttributeError:
            # The node to be removed is the root node
            if node.previous is None:
                node.next.previous = None
                self.root = node.next
            # The node to be removed is the last node
            elif node.next is None:
                node.previous.next = None


double_linked_list = DoublyLinkedList()
double_linked_list.insert_start(12)
double_linked_list.insert_start(10)
double_linked_list.insert_end(10)
double_linked_list.insert_end(23)
double_linked_list.insert_end(40)
double_linked_list.insert_end(55)

double_linked_list.traverse()
print("---------------------------------------------------------------\n")
double_linked_list.search(12)
double_linked_list.search(10)

print("----------------------------------------------------------------\n")
node23 = double_linked_list.search(23)
double_linked_list.remove(node23)
double_linked_list.traverse()
node55 = double_linked_list.search(55)
double_linked_list.remove(node55)
double_linked_list.traverse()
print("-------------------------------------------------------------------\n")
double_linked_list.search(55)
print("-------------------------------------------------------------------\n")
node10 = double_linked_list.search(10)
double_linked_list.remove(node10)
double_linked_list.traverse()
print("---------------------------------------------------------------------\n")
node10 = double_linked_list.search(10)
double_linked_list.remove(node10)
double_linked_list.traverse()
