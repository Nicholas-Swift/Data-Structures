# #!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class BinarySearchTree(object):

    def __init__(self, iterable=None):
        """Initialize this binary search tree and insert the given items if any"""
        self.root = None
        self.size = 0
        if iterable:
            for item in iterable:
                self.insert(item)

    def length(self):
        """Return the length of this binary search tree"""
        return self.size

    def is_empty(self):
        """Return True if this binary search tree contains no nodes"""
        return self.length() == 0

    def search(self, item):
        """Search through the binary search"""
        current = self.root
        while current is not None:
            if item == current.data:
                return True
            if item > current.data:
                current = current.right
            else:
                current = current.left
        return False

    def insert(self, item):
        """Insert a new item into the binary search tree, or assert ValueError if item already exists"""
        if self.root is None:
            self.root = Node(item)
            self.size += 1
            return

        previous = self.root
        current = self.root
        while current is not None:
            if item == current.data:
                assert ValueError("Can not add the same item to a binary search tree")
            if item > current.data:
                previous = current
                current = current.right
            else:
                previous = current
                current = current.left
        if item > previous.data:
            previous.right = Node(item)
        else:
            previous.left = Node(item)
        self.size += 1

    def delete(self, item):
        """Delete an item from the binary search tree, or assert ValueError if item does not exit"""

        if self.root is None:
            assert ValueError("Can not delete from an empty binary search tree")

        if item == self.root.data:

            # Search rightmost of left
            if self.root.left is not None:
                previous = self.root.left
                current = self.root.left
                while current.right is not None:
                    previous = current
                    current = current.right
                if previous != self.root:
                    previous.right = current.right
                    previous.left = current.left
                current.right = self.root.right
                current.left = self.root.left
                self.root = current
                self.size -= 1
                return

            # Search leftmost of right
            elif self.root.right is not None:
                previous = self.root.right
                current = self.root.right
                while current.left is not None:
                    previous = current
                    current = current.left
                if previous != self.root:
                    previous.right = current.right
                    previous.left = current.left
                current.right = self.root.right
                current.left = self.root.left
                self.root = current
                self.size -= 1
                return

            # No left or right, no more tree!
            self.root = None
            self.size -= 1
            return

        # Not the root node
        previous = self.root
        current = self.root
        while current is not None:
            if item == current.data:
                if item > previous.data:
                    if current.right:
                        current.right.left = current.left
                    previous.right = current.right
                else:
                    if current.left:
                        current.left.right = current.right
                    previous.left = current.left
                self.size -= 1
                return
            if item > current.data:
                previous = current
                current = current.right
            else:
                previous = current
                current = current.left
        assert ValueError("Item does not exist in the binary search tree")


def main():
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)
    bst.insert(50)
    bst.insert(49)
    bst.delete(5)


if __name__ == '__main__':
    main()


