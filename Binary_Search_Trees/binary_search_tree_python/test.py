import unittest
from binarySearchTrees_practice import BinarySearchTree


class TestBst(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')
        cls.data1 = 20
        cls.data2 = 15
        cls.data3 = 35
        cls.data4 = 65
        cls.data5 = 17
        cls.data6 = 13
        cls.bst = BinarySearchTree()

    def setUp(self):
        self.bst.insert(self.data1)
        self.bst.insert(self.data2)
        self.bst.insert(self.data3)
        self.bst.insert(self.data4)
        self.bst.insert(self.data5)
        self.bst.insert(self.data6)

    def test_insert(self):
        print('test_insert - test for insert method')
        self.assertEqual(self.bst.root.data, 20)
        self.assertEqual(self.bst.number_of_nodes, 6)

    @classmethod
    def decorator_function(cls, original_function):
        def wrapper(*args, **kwargs):
            return original_function(*args, **kwargs)

        return wrapper

    def test_traverse_in_order(self):
        print('test_traverse_in_order - test for traverse in-order method')
        self.decorator_function(self.bst.traverse_in_order(self.bst.root))
        first_item = self.bst.queue.dequeue()  # O(N) linear running time complexity
        self.assertEqual(first_item.data, 13)
        first_item = self.bst.queue.dequeue()  # O(N-1) linear running time complexity
        self.assertEqual(first_item.data, 15)
        first_item = self.bst.queue.dequeue()  # O(N-2) linear running time complexity
        self.assertEqual(first_item.data, 17)
        first_item = self.bst.queue.dequeue()  # O(N-3) linear running time complexity
        self.assertEqual(first_item.data, 20)

    def test_get_max(self):
        print('test_get_max - test for the maximum value in the BST')
        max_value = self.bst.get_max(self.bst.root)
        self.assertEqual(max_value, 65)

    def test_get_min(self):
        print('test_get_max - test for the maximum value in the BST')
        min_value = self.bst.get_min(self.bst.root)
        self.assertEqual(min_value, 13)

    def test_search(self):
        print('test_search - test for search node method')
        search_result = self.bst.search(17)
        self.assertEqual(search_result.data, 17)
        search_result = self.bst.search(13)
        self.assertEqual(search_result.data, 13)

    def tearDown(self):
        while not self.bst.queue.is_empty():  # O(N) running time complexity
            # del self.bst.queue[-1]  # O(1) constant running time complexity
            self.bst.queue.dequeue()  # O(N) linear running time complexity

    # if we use a dequeue (removing element at the front) for emptying the queue
    # Time complexity for removing every element is O(N)
    # After removing each element the time complexity of shuffling the remaining elements one place to the left
    # for(j = i; j < n; j++){}  => n, (n-1), (n-2), (n-3)...., 3, 2, 1
    # The overall running time complexity is
    # (n) + (n-1) + (n-2) + (n-3) + ..... + 3 + 2 + 1 => n(n+1)/2, so O(n(n+1)/2) = O(n^2)

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


if __name__ == "__main__":
    unittest.main()
