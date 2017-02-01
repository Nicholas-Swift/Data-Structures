#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any"""
        """Best case Omega(1)"""
        """Worst case O(n)"""
        self.head = None
        self.tail = None
        self.size = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def __getitem__(self, arg):
        """Get the item at the index, or raise KeyError if not an int"""
        """Best case Omega(1)"""
        """Worst case O(n)"""
        if type(arg) is not int:
            raise TypeError

        # If argument is over list size, raise ValueError
        if arg >= self.length() or arg < -self.length():
            raise IndexError

        # Use modulus operator, so index can use negatives
        counter = arg % self.length()
        currentIndex = 0

        if counter == self.length():
            return self.last()

        current = self.head
        while current is not None:
            if counter == currentIndex:
                return current.data
            currentIndex += 1
            current = current.next

    def as_list(self):
        """Return a list of all items in this linked list"""
        """Best case Omega(1)"""
        """Worst case O(n)"""
        items = []
        current = self.head
        while current is not None:
            items.append(current.data)
            current = current.next
        return items

    def is_empty(self):
        """Return True if this linked list is empty, or False otherwise"""
        """Best case Omega(1)"""
        """Worst case O(1)"""
        return self.head is None

    def length(self):
        """Return the length of this linked list"""
        """Best case Omega(1)"""
        """Worst case O(1)"""
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        """Best case Omega(1)"""
        """Worst case O(1)"""
        new_node = Node(item)
        # Check if list is empty
        if self.head is None:
            self.head = new_node
        # Otherwise insert after tail node
        else:
            self.tail.next = new_node
        # Update tail node
        self.tail = new_node
        # Update length
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        """Best case Omega(1)"""
        """Worst case O(1)"""
        new_node = Node(item)
        # Insert before head node
        new_node.next = self.head
        # Update head node
        self.head = new_node
        # Check if list was empty
        if self.tail is None:
            self.tail = new_node
        # Update length
        self.size += 1

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        """Best case Omega(1)"""
        """Worst case O(n)"""
        current = self.head
        previous = None
        found = False
        # Find the given item
        while not found and current is not None:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        # Delete if found
        if found:
            if current is not self.head and current is not self.tail:
                previous.next = current.next
                current.next = None
            if current is self.head:
                self.head = current.next
            if current is self.tail:
                if previous is not None:
                    previous.next = None
                self.tail = previous
            # Update length
            self.size -= 1
        else:
            raise ValueError('Item not found: {}'.format(item))

    def delete_at_index(self, index):
        """Delete the item at the given index from this linked list, or raise ValueError"""

        if type(index) is not int:
            raise TypeError

        # If argument is over list size, raise ValueError
        if index >= self.length() or index < -self.length():
            raise IndexError

        # Use modulus operator, so index can use negatives
        counter = index % self.length()
        currentIndex = 0

        current = self.head
        previous = None
        found = False

        # Find the given item
        while not found and current is not None:
            if currentIndex == counter:
                found = True
            else:
                previous = current
                current = current.next
                currentIndex += 1
        if found:
            if current is not self.head and current is not self.tail:
                previous.next = current.next
                current.next = None
            if current is self.head:
                self.head = current.next
            if current is self.tail:
                if previous is not None:
                    previous.next = None
                self.tail = previous
            # Update length
            self.size -= 1
        else:
            raise ValueError('Item not found: {}'.format(item))

        pass

    def find(self, condition):
        """Return an item in this linked list satisfying the given condition"""
        """Best case Omega(1)"""
        """Worst case O(n)"""
        current = self.head  # Start at the head node
        while current is not None:
            if condition(current.data):
                return current.data
            current = current.next  # Skip to the next node
        return None


if __name__ == '__main__':
    test_linked_list()
