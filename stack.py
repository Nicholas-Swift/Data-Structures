#!python
from linkedlist import LinkedList
from queue import PriorityQueue

# """Stack built with array"""
# class Stack(list):

#     def __init__(self, iterable=None):
#         """Initialize this stack and push the given items, if any"""
#         super(Stack, self).__init__()
#         if iterable:
#             for item in iterable:
#                 self.push(item)

#     def __repr__(self):
#         """Return a string representation of this stack"""
#         return 'Stack({})'.format(self.length())

#     def is_empty(self):
#         """Return True if this stack is empty, or False otherwise"""
#         return len(self) == 0

#     def length(self):
#         """Return the number of items in this stack"""
#         return len(self)

#     def peek(self):
#         """Return the top item on this stack without removing it, or None if this stack is empty"""
#         return None if self.is_empty() else self[-1] 

#     def push(self, item):
#         """Push the given item onto this stack"""
#         self.append(item)

#     def pop(self):
#         """Return the top item and remove it from this stack, or raise ValueError if this stack is empty"""
#         if self.is_empty:
#             raise ValueError
#         else:
#             return super(Stack, self).pop()


# """Stack built with linked list"""
# class Stack(LinkedList):

#     def __init__(self, iterable=None):
#         """Initialize this stack and push the given items, if any"""
#         super(Stack, self).__init__()
#         if iterable:
#             for item in iterable:
#                 self.push(item)

#     def __repr__(self):
#         """Return a string representation of this stack"""
#         return 'Stack({})'.format(self.length())

#     def is_empty(self):
#         """Return True if this stack is empty, or False otherwise"""
#         return super(Stack, self).is_empty()

#     def length(self):
#         """Return the number of items in this stack"""
#         return self.size

#     def peek(self):
#         """Return the top item on this stack without removing it, or None if this stack is empty"""
#         return None if self.is_empty() else self[-1]

#     def push(self, item):
#         """Push the given item onto this stack"""
#         self.append(item)

#     def pop(self):
#         """Return the top item and remove it from this stack, or raise ValueError if this stack is empty"""
#         if self.is_empty():
#             raise ValueError
#         else:
#             item = self[-1]
#             self.delete_at_index(-1)
#             return item


"""Stack built with priority queue"""
class Stack(PriorityQueue):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        super(Stack, self).__init__()
        self.current_priority = 0
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({})'.format(self.length())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        return super(Stack, self).is_empty()

    def length(self):
        """Return the number of items in this stack"""
        return self.size

    def peek(self):
        """Return the top item on this stack without removing it, or None if this stack is empty"""
        return super(Stack, self).peek()

    def push(self, item):
        """Push the given item onto this stack"""
        self.enqueue(self.current_priority, item)
        self.current_priority -= 1

    def pop(self):
        """Return the top item and remove it from this stack, or raise ValueError if this stack is empty"""
        return self.dequeue()
