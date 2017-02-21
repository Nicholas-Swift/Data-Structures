#!python

class MinHeap(object):
    """A MinHeap is an unordered collection with access to its minimum item,
    and provides efficient methods for insertion and removal of its minimum."""

    def __init__(self):
        """Initialize this min heap with an empty list of items"""
        self.items = []

    def __repr__(self):
        """Return a string representation of this min heap"""
        return 'MinHeap({})'.format(self.items)

    def __len__(self):
        return self.size()

    def size(self):
        """Return the number of items in the heap"""
        return len(self.items)

    def peek(self):
        return self.get_min()

    def get_min(self):
        """Return the minimum item at the root of the heap"""
        if self.size() < 1:
            raise ValueError('Heap is empty and has no minimum item')

        # print(self.items)

        return self.items[0]

    def pop(self):
        return self.remove_min()

    def remove_min(self):
        """Remove and return the minimum item at the root of the heap"""
        if self.size() < 1:
            raise ValueError('Heap is empty and has no minimum item')

        if self.size() == 1:
            # Remove and return the only item
            return self.items.pop()

        assert self.size() > 1
        min_item = self.items[0]

        # Move the last item to the root and bubble down to the leaves
        last_item = self.items.pop()
        self.items[0] = last_item

        if self.size() > 1:
            self._bubble_down(0)

        return min_item

    def push_pop(self, item):
        return self.replace_min(item)

    def replace_min(self, item):
        """Remove and return the minimum and insert a new item into the heap"""
        if self.size() < 1:
            raise ValueError('Heap is empty and has no minimum item')

        min_item = self.items[0]

        # Replace the root and bubble down to the leaves
        self.items[0] = item
        if self.size() > 1:
            self._bubble_down(0)

        return min_item

    def push(self, item):
        self.insert(item)

    def insert(self, item):
        """Insert an item into the heap"""
        # Insert the item at the end and bubble up to the root
        self.items.append(item)
        if self.size() > 1:
            self._bubble_up(self._last_index())

    def _bubble_up(self, index):
        """Ensure the heap-ordering property is true above the given index,
        swapping out of order items, or until the root node is reached"""

        if index == 0:
            return  # This index is the root node

        if not (0 <= index <= self._last_index()):
            raise IndexError('Invalid index: {}'.format(index))

        item = self.items[index]

        # Swap this item with parent item if values are out of order
        parent_index = self._parent_index(index)
        parent_item = self.items[parent_index]
        if item < parent_item:
            self.items[index], self.items[parent_index] = parent_item, item

            # Then bubble up again if necessary
            self._bubble_up(parent_index)

    def _bubble_down(self, index):
        """Ensure the heap-ordering property is true below the given index,
        swapping out of order items, or until a leaf node is reached"""

        if not (0 <= index <= self._last_index()):
            raise IndexError('Invalid index: {}'.format(index))

        left_index = self._left_child_index(index)
        right_index = self._right_child_index(index)
        if left_index > self._last_index():
            return  # This index is a leaf node (does not have any children)

        item = self.items[index]

        # Determine which child item to compare this node's item to
        if left_index > self.size() - 1:
            return
        elif right_index > self.size() - 1:
            child_index = left_index
        else:
            child_index = left_index if self.items[left_index] < self.items[right_index] else right_index

        # Swap this item with a child item if values are out of order
        child_item = self.items[child_index]

        if item > child_item:
            self.items[index], self.items[child_index] = child_item, item

            # Then bubble down again if necessary
            self._bubble_down(child_index)

    def _last_index(self):
        """Return the last valid index in the underlying array of items"""
        return len(self.items) - 1

    def _parent_index(self, index):
        """Return the parent index of the item at the given index"""
        if index < 1:
            raise IndexError('Heap index {} has no parent index'.format(index))
        return (index - 1) >> 1

    def _left_child_index(self, index):
        """Return the left child index of the item at the given index"""
        return (index << 1) + 1

    def _right_child_index(self, index):
        """Return the right child index of the item at the given index"""
        return (index << 1) + 2
