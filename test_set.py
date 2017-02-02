#!python

from set import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        q = Set()
        assert q.length() == 0

    def test_length(self):
        q = Set()
        assert q.length() == 0
        q.add('one')
        assert q.length() == 1
        q.add('fish')
        assert q.length() == 2
        q.add('two')
        q.add('red')
        q.add('blue')
        assert q.length() == 5
        q.remove('fish')
        assert q.length() == 4
        q.remove('two')
        assert q.length() == 3
        q.remove('one')
        q.remove('red')
        q.remove('blue')
        assert q.length() == 0

    def test_items(self):
        q = Set()
        q.add('one')
        q.add('fish')
        q.add('two')
        q.add('red')
        q.add('blue')
        assert all(item in q.items() for item in ['one', 'fish', 'two', 'red', 'blue']) == True
        q.remove('blue')
        assert all(item in q.items() for item in ['one', 'fish', 'two', 'red', 'blue']) == False
        assert all(item in q.items() for item in ['one', 'fish', 'two', 'red']) == True

    def test_clear(self):
        q = Set()
        q.add('one')
        q.add('fish')
        q.add('two')
        q.add('red')
        q.add('blue')
        q.clear()
        assert q.length() == 0
        assert q.items() == []

    def test_load(self):
        q = Set(6)
        assert q.load == 0
        q.add('one')
        assert q.load == 1/float(6)
        q.add('fish')
        assert q.load == 2/float(6)
        q.add('two')
        q.add('red')
        assert q.load == 4/float(6)
        q.add('blue')
        assert q.load == 5/float(12)


if __name__ == '__main__':
    unittest.main()
