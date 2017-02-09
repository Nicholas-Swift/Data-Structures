#!python

from binarysearchtree import BinarySearchTree, Node
import unittest


class NodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        node = Node(data)
        assert node.data is data
        assert node.right is None
        assert node.left is None


class LinkedListTest(unittest.TestCase):

    def test_init(self):
        bst = BinarySearchTree()
        assert bst.root is None
        assert bst.is_empty() is True

    def test_init_with_list(self):
        bst = BinarySearchTree(['B', 'A', 'C'])
        assert bst.root.data == 'B'
        assert bst.root.right.data == 'C'
        assert bst.root.left.data == 'A'
        assert bst.is_empty() is False

    def test_length(self):
        bst = BinarySearchTree()
        assert bst.length() == 0
        bst.insert('A')
        assert bst.length() == 1
        bst.insert('B')
        assert bst.length() == 2
        bst.insert('C')
        assert bst.length() == 3
        bst.delete('C')
        assert bst.length() == 2
        bst.delete('B')
        assert bst.length() == 1
        bst.delete('A')
        assert bst.length() == 0

    def test_search(self):
        bst = BinarySearchTree(['A', 'B', 'C'])
        assert bst.search('A') == True
        assert bst.search('B') == True
        assert bst.search('C') == True
        assert bst.search('D') == False

    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert(10)
        assert bst.root.data == 10
        bst.insert(5)
        assert bst.root.data == 10
        assert bst.root.left.data == 5
        bst.insert(7)
        assert bst.root.data == 10
        assert bst.root.left.data == 5
        assert bst.root.left.right.data == 7

    def test_delete(self):
        bst = BinarySearchTree([10, 5, 1, 8, 15, 11, 18])

        bst.delete(18)
        assert bst.root.data == 10
        assert bst.root.left.data == 5
        assert bst.root.left.left.data == 1
        assert bst.root.left.right.data == 8
        assert bst.root.right.data == 15
        assert bst.root.right.left.data == 11
        assert bst.root.right.right == None
        assert bst.search(18) == False

        bst = BinarySearchTree([10, 5, 1, 8, 15, 11, 18])
        bst.delete(15)
        assert bst.root.data == 10
        assert bst.root.left.data == 5
        assert bst.root.left.left.data == 1
        assert bst.root.left.right.data == 8
        assert bst.root.right.data == 11
        assert bst.root.right.right.data == 18
        assert bst.root.right.left == None
        assert bst.search(15) == False

        bst = BinarySearchTree([10, 5, 1, 8, 15, 11, 18])
        bst.delete(10)
        assert bst.root.data == 8
        assert bst.root.left.data == 5
        assert bst.root.left.left.data == 1
        assert bst.root.left.right == None
        assert bst.root.right.data == 15
        assert bst.root.right.right.data == 18
        assert bst.root.right.left.data == 11

    def test_in_order_traversal(self):
        bst = BinarySearchTree([10, 20, 15, 25, 23, 22, 30])
        assert bst.in_order_traversal() == [10, 15, 20, 22, 23, 25, 30]
        bst = BinarySearchTree([10,50,5,9,1,3,2])
        assert bst.in_order_traversal() == [1,2,3,5,9,10,50]

    def test_pre_order_traversal(self):
        bst = BinarySearchTree([10, 20, 15, 25, 23, 22, 30])
        assert bst.pre_order_traversal() == [10, 20, 15, 25, 23, 22, 30]
        bst = BinarySearchTree([10,50,5,9,1,3,2])
        assert bst.pre_order_traversal() == [10,5,1,3,2,9,50]

    def test_post_order_traversal(self):
        bst = BinarySearchTree([10, 20, 15, 25, 23, 22, 30])
        assert bst.post_order_traversal() == [15, 22, 23, 30, 25, 20, 10]
        bst = BinarySearchTree([10,50,5,9,1,3,2])
        assert bst.post_order_traversal() == [2,3,1,9,5,50,10]


if __name__ == '__main__':
    unittest.main()
