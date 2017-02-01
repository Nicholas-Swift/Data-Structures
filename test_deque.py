#!python

from deque import Deque
import unittest


class QueueTest(unittest.TestCase):

    def test_init(self):
        q = Deque()
        assert q.peekLeft() is None
        assert q.peekRight() is None
        assert q.length() == 0
        assert q.is_empty() is True

    def test_init_with_list(self):
        q = Deque(['A', 'B', 'C'])
        assert q.peekLeft() == 'A'
        assert q.peekRight() == 'C'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_length_with_push_and_pop_right(self):
        q = Deque()
        assert q.length() == 0
        q.pushRight('A')
        assert q.length() == 1
        q.pushRight('B')
        assert q.length() == 2
        q.popRight()
        assert q.length() == 1
        q.popRight()
        assert q.length() == 0

    def test_length_with_push_and_pop_left(self):
        q = Deque()
        assert q.length() == 0
        q.pushLeft('A')
        assert q.length() == 1
        q.pushLeft('B')
        assert q.length() == 2
        q.popLeft()
        assert q.length() == 1
        q.popLeft()
        assert q.length() == 0

    def test_length_with_push_and_pop_left_and_right(self):
        q = Deque()
        assert q.length() == 0
        q.pushRight('A')
        assert q.length() == 1
        q.pushLeft('B')
        assert q.length() == 2
        q.popRight()
        assert q.length() == 1
        q.popLeft()
        assert q.length() == 0

    def test_peek_left_and_right(self):
        q = Deque()
        assert q.peekLeft() is None
        q.pushRight('A')
        assert q.peekLeft() == 'A'
        assert q.peekRight() == 'A'
        q.pushRight('B')
        assert q.peekLeft() == 'A'
        assert q.peekRight() == 'B'
        q.popRight()
        assert q.peekRight() == 'A'
        q.popRight()
        assert q.peekLeft() is None

    def test_push_right_and_left(self):
        q = Deque()
        q.pushLeft('A')
        q.pushRight('B')
        assert q.peekLeft() == 'A'
        assert q.peekRight() == 'B'
        q.pushRight('C')
        assert q.peekLeft() == 'A'
        assert q.peekRight() == 'C'
        q.pushLeft('Z')
        assert q.peekLeft() == 'Z'
        assert q.peekRight() == 'C'


if __name__ == '__main__':
    unittest.main()
