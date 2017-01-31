#!python
from linkedlist import LinkedList

# """Queue built with array"""
# class Queue(list):

#     def __init__(self, iterable=None):
#         """Initialize this queue and enqueue the given items, if any"""
#         super(Queue, self).__init__()
#         if iterable:
#             for item in iterable:
#                 self.enqueue(item)

#     def __repr__(self):
#         """Return a string representation of this queue"""
#         return 'Queue({})'.format(self.length())

#     def is_empty(self):
#         """Return True if this queue is empty, or False otherwise"""
#         return len(self) == 0

#     def length(self):
#         """Return the number of items in this queue"""
#         return len(self)

#     def peek(self):
#         """Return the next item in this queue without removing it, or None if this queue is empty"""
#         return None if self.is_empty() else self[0]

#     def enqueue(self, item):
#         """Enqueue the given item into this queue"""
#         self.append(item)

#     def dequeue(self):
#         """Return the next item and remove it from this queue, or raise ValueError if this queue is empty"""
#         if self.is_empty():
#             raise ValueError
#         else:
#             return self.pop(0)


"""Queue built with linked list"""
class Queue(LinkedList):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        super(Queue, self).__init__()
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({})'.format(self.length())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        return super(Queue, self).is_empty()

    def length(self):
        """Return the number of items in this queue"""
        return self.size

    def peek(self):
        """Return the next item in this queue without removing it, or None if this queue is empty"""
        return None if self.is_empty() else self.first()

    def enqueue(self, item):
        """Enqueue the given item into this queue"""
        self.append(item)

    def dequeue(self):
        """Return the next item and remove it from this queue, or raise ValueError if this queue is empty"""
        if self.is_empty():
            raise ValueError
        else:
            item = self.first()
            self.delete(item)
            return item
