# #!python

from binarysearchtree import BinarySearchTree

class Map(BinarySearchTree):

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

    def _leftmost_node_and_previous(self, start_node):
        """Find the leftmost node in the subtree"""
        previous = start_node
        current = start_node
        while current.left is not None:
            previous = current
            current = current.left
        return (current, previous)

    def _rightmost_node_and_previous(self, start_node):
        """Find the rightmost node in the subtree"""
        previous = start_node
        current = start_node
        while current.right is not None:
            previous = current
            current = current.right
        return (current, previous)

    def _reassign_root(self, new_node):
        new_node.right = self.root.right
        new_node.left = self.root.left
        self.root = new_node

    def delete(self, item):
        """Delete an item from the binary search tree, or assert ValueError if item does not exit"""

        if self.root is None:
            assert ValueError("Can not delete from an empty binary search tree")

        # Find the node to delete and it's previous node
        previous = self.root
        current = self.root
        while current is not None:
            if item == current.data:
                break
            elif item > current.data:
                previous = current
                current = current.right
            else:
                previous = current
                current = current.left

        # Assert ValueError if the node was not found
        if current is None:
            assert ValueError("Item does not exist in the binary search tree")

        # Delete the item
        if current.left is not None:
            rightmost, rightmost_parent = self._rightmost_node_and_previous(current.left)
            rightmost_parent.right = rightmost.left

            if current == self.root:
                self._reassign_root(rightmost)
                self.size += 1
                return

            rightmost.right = current.right
            if current.data > previous.data:
                previous.right = rightmost
            else:
                previous.left = rightmost

        elif current.right is not None:
            leftmost, leftmost_parent = self._leftmost_node_and_previous(current.right)
            leftmost_parent.left = leftmost.right

            if current == self.root:
                self._reassign_root(leftmost)
                self.size += 1
                return

            leftmost.left = current.left
            if current.data > previous.data:
                previous.right = leftmost
            else:
                previous.left = leftmost

        else:
            if current.data == previous.data: # self.root
                self.root = None
            elif current.data > previous.data:
                previous.right = None
            else:
                previous.left = None

        self.size -= 1

    def in_order_traversal(self, current_node=None, return_list=None):
        """Perform an in-order traversal on the binary search tree and return a list of nodes"""

        # Set up current_node and current_node if first iteration
        if return_list is None:
            return_list = []
        if current_node is None:
            current_node = self.root

        # Traverse left
        if current_node.left is not None:
            self.in_order_traversal(current_node.left, return_list)

        # Append current
        return_list.append(current_node.data)

        # Traverse right
        if current_node.right is not None:
            self.in_order_traversal(current_node.right, return_list)
        
        return return_list

    def pre_order_traversal(self, current_node=None, return_list=None):
        """Perform an pre-order traversal on the binary search tree and return a list of nodes"""

        # Set up current_node and current_node if first iteration
        if return_list is None:
            return_list = []
        if current_node is None:
            current_node = self.root

        # Append current
        return_list.append(current_node.data)

        # Traverse left
        if current_node.left is not None:
            self.pre_order_traversal(current_node.left, return_list)

        # Traverse right
        if current_node.right is not None:
            self.pre_order_traversal(current_node.right, return_list)
        
        return return_list

    def post_order_traversal(self, current_node=None, return_list=None):
        """Perform an post-order traversal on the binary search tree and return a list of nodes"""
        
        # Set up current_node and current_node if first iteration
        if return_list is None:
            return_list = []
        if current_node is None:
            current_node = self.root

        # Traverse left
        if current_node.left is not None:
            self.post_order_traversal(current_node.left, return_list)

        # Traverse right
        if current_node.right is not None:
            self.post_order_traversal(current_node.right, return_list)

        # Append current
        return_list.append(current_node.data)

        return return_list


def main():
    bst = BinarySearchTree([5, 1, 6, 8, 9, 2, 11])
    print(bst.in_order_traversal())


if __name__ == '__main__':
    main()


