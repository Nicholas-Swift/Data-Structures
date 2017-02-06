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
        bst = BinarySearchTree([50, 20, 19, 25, 17, 18, 28, 59, 58, 60])
        bst.delete(60)
        assert bst.root.data == 50
        assert bst.root.right.right == None
        assert bst.search(60) == False
        bst.delete(20)
        assert bst.root.data == 50
        assert bst.root.left.data == 19
        assert bst.root.left.right.data == 25
        assert bst.search(20) == False
        bst.delete(50)
        assert bst.root.data == 28
        assert bst.root.right.data == 59
        assert bst.root.left.data == 19
        assert bst.root.left.right.data == 25
        assert bst.root.left.left.data == 17
        assert bst.root.left.left.right.data == 18
        assert bst.search(50) == False


if __name__ == '__main__':
    unittest.main()
