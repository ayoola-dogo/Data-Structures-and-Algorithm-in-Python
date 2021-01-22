class Node:
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.Num_of_nodes = 0

    def insert(self, data):
        if self.root is None:
            node = Node(data, parent=None)
            self.root = node
        else:
            self.insert_node(data, node=self.root)

    # The insertion has a O(log N) logarithmic running time complexity - for a balanced tree
    def insert_node(self, data, node):
        # Make the node the current node
        current_node = node
        # check if the data to be inserted is less than the current node data
        if data < current_node.data:
            # if it is, go to the left edge and check the left child/subtree
            if current_node.leftChild is not None:
                self.insert_node(data, current_node.leftChild)
            else:
                # make the current_node the parent node
                parent_node = current_node
                new_node = Node(data, parent_node)
                parent_node.leftChild = new_node
        elif data > current_node.data:
            # if it is, go to the right edge and check the right child/subtree
            if current_node.rightChild is not None:
                self.insert_node(data, current_node.rightChild)
            else:
                # make the current_node the parent node
                parent_node = current_node
                new_node = Node(data, parent_node)
                parent_node.rightChild = new_node

    # Traverse a binary search tree
    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    # My implementation (I think it's more efficient as I only use a while loop)
    # def get_max_value(self):
    #     if self.root:
    #         current_node = self.root
    #         while current_node.rightChild is not None:
    #             current_node = current_node.rightChild
    #         print("The maximum value in the BST:", current_node.data)

    # The Tutorial implementation //Uses the while and Stack ADT. Might be less efficient compared to my implementation
    # Still have the same running time complexity with my implementation as the stack pop operation has O(1) complexity
    def max_value(self):
        if self.root:
            return self.get_max(self.root).data

    def get_max(self, node):
        if node.rightChild:
            return self.get_max(node.rightChild)
        return node

    def min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.leftChild:
            return self.get_max(node.leftChild)
        return node.data

    # implementing the in-order traversal for Binary Search Tree
    def traverse_in_order(self, node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)
        print(node.data)
        if node.rightChild:
            self.traverse_in_order(node.rightChild)

    # Removing a node in a Binary Search Tree has O(log N) logarithmic running time complexity
    def remove(self, data):
        if self.root:
            self.remove_node(data, node=self.root)

    def remove_node(self, data, node):
        # search operation
        removal_node = self.search(data, node)

        if removal_node:
            # check if it is either a leaf, one childed, or two childed node
            # Leaf Node
            if removal_node.leftChild is None and removal_node.rightChild is None:
                self.remove_leaf_node(removal_node)
            # One childed node
            elif removal_node.leftChild is None or removal_node.rightChild is None:
                self.remove_one_childed_node(removal_node)
            # Two childed node
            if removal_node.leftChild and removal_node.rightChild:
                self.remove_two_childed_node(removal_node)

    # This operation has the O(log N) logarithmic running time complexity
    def search(self, data, node):
        # Make the node the current node
        current_node = node
        # Base Case - when the base case is hits, pass and do nothing - progress to the next line of code
        if data == current_node.data:
            return current_node
        elif data < current_node.data:
            if current_node.leftChild:
                current_node = current_node.leftChild
                return self.search(data, current_node)
        elif data > current_node.data:
            if current_node.rightChild:
                current_node = current_node.rightChild
                return self.search(data, current_node)
        return

    def remove_leaf_node(self, node):
        # Leaf Node
        parent = node.parent
        if parent is not None and parent.leftChild == node:
            parent.leftChild = None
        elif parent is not None and parent.rightChild == node:
            parent.rightChild = None

        if parent is None:
            self.root = None

        del node

    def remove_one_childed_node(self, node):
        if node.leftChild:
            if node.parent is not None:
                node.leftChild.parent = node.parent
                if node.parent.leftChild == node:
                    node.parent.leftChild = node.leftChild
                elif node.parent.rightChild == node:
                    node.parent.rightChild = node.leftChild
            else:
                node.leftChild.parent = None
                self.root = node.leftChild
        elif node.rightChild:
            if node.parent:
                node.rightChild.parent = node.parent
                if node.parent.leftChild == node:
                    node.parent.leftChild = node.rightChild
                elif node.parent.rightChild == node:
                    node.parent.rightChild = node.rightChild
            else:
                node.rightChild.parent = None
                self.root = node.rightChild
        del node

    def remove_two_childed_node(self, node):
        # Find largest item in the left subtree
        pred_node = self.get_max(node.leftChild)
        # Swap predecessor with the node that needs to removed
        temp = node.data
        node.data = pred_node.data
        pred_node.data = temp
        # check if the largest item in the left subtree is a leaf or single childed node (leftChild node)
        if pred_node.leftChild:
            self.remove_one_childed_node(pred_node)
        else:
            self.remove_leaf_node(pred_node)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(99)
bst.insert(-5)
bst.insert(34)
bst.insert(1)
bst.insert(100)
bst.insert(99.5)
bst.insert(30)
bst.insert(-10)
bst.insert(120)
bst.insert(110)
bst.insert(140)
bst.traverse()
print("----------------------------------------------------------------------------")
maxm = bst.max_value()
print(maxm)
print("--------------------------Remove Node----------------------------------------")
bst.remove(0)
print("----------------------------------------------------------------------------")
bst.traverse()
# print(bst.root.data)
# print(bst.root.leftChild.data)
