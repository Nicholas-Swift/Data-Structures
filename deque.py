#!python
from linkedlist import LinkedList


class Deque(LinkedList):

    def __init__(self, iterable=None):
        """Initialize this deque and pushRight the given items, if any"""
        super(Deque, self).__init__()
        if iterable:
            for item in iterable:
                self.pushRight(item)

    def __repr__(self):
        return 'Deque({})'.format(self.length())

    def is_empty(self):
        return super(Deque, self).is_empty()

    def length(self):
        return self.size

    def peekRight(self):
        return None if self.is_empty() else self[-1]

    def peekLeft(self):
        return None if self.is_empty() else self[0]

    def pushRight(self, item):
        self.append(item)

    def pushLeft(self, item):
        self.prepend(item)

    def popRight(self):
        if self.is_empty():
            raise ValueError
        else:
            item = self[-1]
            self.delete_at_index(-1)
            return item

    def popLeft(self):
        if self.is_empty():
            raise ValueError
        else:
            item = self[0]
            self.delete_at_index(0)
            return item
