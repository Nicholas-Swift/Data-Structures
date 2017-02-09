# #!python

from binarysearchtree import BinarySearchTree

class Map(BinarySearchTree):

    def __init__(self):
        """Initialize this binary search tree and insert the given items if any"""
        super(Map, self).__init__()

    def __contains__(self):
        """Does it contain the item"""
        return 

    def length(self):
        """Return the length of this binary search tree"""
        return super(Map, self).length()

    def is_empty(self):
        """Return True if this binary search tree contains no nodes"""
        return self.length() == 0

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        pass

    def get(self, key):
        """Return the value associated with the given key, or return None"""
        pass

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        pass

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        pass

    def keys(self):
        """Return a list of all keys in this hash table"""
        pass

    def values(self):
        """Return a list of all values in this hash table"""
        pass

    def items(self):
        """Return a list of all items (key, value) in this hash table"""
        pass


def main():
    bst = BinarySearchTree([5, 1, 6, 8, 9, 2, 11])
    print(bst.in_order_traversal())


if __name__ == '__main__':
    main()


