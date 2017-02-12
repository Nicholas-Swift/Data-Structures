# #!python

class Node(object):

    def __init__(self, first_data, second_data=None):
        """Initialize this node with the given data"""
        self.first_data = first_data
        self.second_data = second_data
        self.left = None
        self.middle = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({}, {})'.format(repr(self.first_data), repr(self.second_data))
        # return 'Node({})'.format(repr(self.data))

    def insert(self, item):
        """Insert an item into the node"""

        # Same item, value error
        if item == self.first_data or item == self.second_data:
            assert ValueError("Item already exists in the binary search tree")

        # First data is None, add the item and return
        if self.first_data is None:
            self.first_data = item
            return

        # Second data is None, add the item to correct order
        if self.second_data is None:
            self.first_data, self.second_data = (self.first_data, item) if item > self.first_data else (item, self.first_data)
            return

        # Both are full, pop something!
        if item > self.second_data:
            popped_data = self.second_data
            self.second_data = item
            return popped_data
        else:
            popped_data = self.first_data
            self.first_data = item
            return popped_data


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
        """Search through the binary search tree"""
        current = self.root
        while current is not None:
            if item == current.first_data or item == current.second_data:
                return True
            if item > current.first_data and item < current.second_data:
                current = current.middle
            elif item > current.second_data:
                current = current.right
            else:
                current = current.left
        return False

    def insert(self, item):
        """Insert a new item into the binary search tree, or assert ValueError if item already exists"""

        # Set to root
        if self.root is None:
            self.root = Node(item)
            return

        current = self.root
        insert_item = self.insert_helper(item, current)

        # Create new root
        if insert_item:
            old_root = current
            self.root = Node(insert_item)

            if old_root.left is None:
                self.root.left = Node(old_root.first_data)
                self.root.right = Node(old_root.second_data)
            else:
                self.root.left = old_root.left
                self.root.right = old_root.right

    def insert_helper(self, item, current):

        if item > current.first_data and item < current.second_data and current.middle is not None:
            self.insert_helper(item, current.middle)
        elif item > current.second_data and current.right is not None:
            self.insert_helper(item, current.right)
        elif item < current.first_data and current.left is not None:
            self.insert_helper(item, current.left)

        return current.insert(item)


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
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)

    print('\n')
    print(bst.root)
    print(bst.root.right)
    print(bst.root.left)
    print('\n')


if __name__ == '__main__':
    main()


