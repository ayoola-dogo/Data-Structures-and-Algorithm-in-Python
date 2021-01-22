class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        try:
            return "data({0})||next({1})".format(self.data, self.next.data)
        except AttributeError:
            return "data({0})||next(None)".format(self.data)


class LinkedList:

    def __init__(self):
        self.root = None
        self.num_of_nodes = 0

    @staticmethod
    def create_node(data):
        node = Node(data)
        return node

    # Ordo 1 O(1) constant running time complexity
    def size_of_linked_list(self):
        return self.num_of_nodes

    # O(N) linear running time complexity
    def traverse(self):
        actual_node = self.root

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next

    # This has a O(N) running time complexity
    def search(self, data):
        actual_node = self.root

        while actual_node is not None and actual_node.data != data:
            actual_node = actual_node.next
        if actual_node is None:
            print("data not found")
        else:
            print("node:", actual_node)

    # constant running time O(1)
    def insert_start(self, data):
        node = self.create_node(data)
        if self.root is None:
            self.root = node
        else:
            node.next = self.root
            self.root = node
        self.num_of_nodes += 1

    # linear running time O(N)
    def insert_end(self, data):
        node = Node(data)
        actual_node = self.root

        while actual_node.next is not None:
            actual_node = actual_node.next
        else:
            actual_node.next = node
            self.num_of_nodes += 1

    def remove(self, data):
        node = self.create_node(data)
        # empty linked_list
        if self.root is None:
            return

        # Removing at the start - the root node. The running time complexity is O(1)
        if self.root.data == node.data:
            self.root = self.root.next
            self.num_of_nodes -= 1
        else:
            # Removing anywhere else in the linked_list. The running time complexity is O(N)
            actual_node = self.root
            previous_node = None
            while actual_node is not None and actual_node.data != node.data:
                previous_node = actual_node
                actual_node = actual_node.next

            # Value not in linked_list
            if actual_node is None:
                return
            # Value found within the linked list
            previous_node.next = actual_node.next
            self.num_of_nodes -= 1


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_start(23)
    linked_list.insert_start(10)
    linked_list.insert_start(3)
    linked_list.insert_end(100)
    linked_list.insert_end(150)
    print('There are ', linked_list.num_of_nodes, 'nodes in the linked list')
    linked_list.traverse()
    print("-----------------------------------------------------------------------")
    linked_list.remove(23)
    print('There are ', linked_list.num_of_nodes, 'nodes in the linked list')
    linked_list.traverse()
    print("-----------------------------------------------------------------------")
    linked_list.search(10)
