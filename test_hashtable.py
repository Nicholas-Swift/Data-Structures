#!python

from hashtable import HashTable
import unittest


class HashTableTest(unittest.TestCase):

    def test_init(self):
        q = HashTable()
        assert q.length() == 0

    def test_length(self):
        q = HashTable()
        assert q.length() == 0
        q.set('one', 1)
        assert q.length() == 1
        q.set('fish', 4)
        assert q.length() == 2
        q.set('two', 1)
        q.set('red', 1)
        q.set('blue', 1)
        assert q.length() == 5
        q.delete('fish')
        assert q.length() == 4
        q.delete('two')
        assert q.length() == 3
        q.delete('one')
        q.delete('red')
        q.delete('blue')
        assert q.length() == 0

    def test_keys(self):
        q = HashTable()
        q.set('one', 1)
        q.set('fish', 4)
        q.set('two', 1)
        q.set('red', 1)
        q.set('blue', 1)
        assert all(item in q.keys() for item in ['one', 'fish', 'two', 'red', 'blue']) == True
        q.delete('blue')
        assert all(item in q.keys() for item in ['one', 'fish', 'two', 'red', 'blue']) == False
        assert all(item in q.keys() for item in ['one', 'fish', 'two', 'red']) == True

    def test_values(self):
        q = HashTable()
        q.set('one', 1)
        q.set('fish', 4)
        q.set('two', 1)
        q.set('red', 1)
        q.set('blue', 1)
        assert all(item in q.values() for item in [1, 4, 1, 1, 1]) == True
        q.delete('blue')
        assert all(item in q.values() for item in [1, 4, 1, 1]) == True

    def test_items(self):
        q = HashTable()
        q.set('one', 1)
        q.set('fish', 4)
        q.set('two', 1)
        q.set('red', 1)
        q.set('blue', 1)
        assert all(item in q.items() for item in [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]) == True

    def test_clear(self):
        q = HashTable()
        q.set('one', 1)
        q.set('fish', 4)
        q.set('two', 1)
        q.set('red', 1)
        q.set('blue', 1)
        q.clear()
        assert q.length() == 0
        assert q.items() == []

    def test_load(self):
        q = HashTable(6)
        assert q.load == 0
        q.set('one', 1)
        assert q.load == 1/float(6)
        q.set('fish', 4)
        assert q.load == 2/float(6)
        q.set('two', 1)
        q.set('red', 1)
        assert q.load == 4/float(6)
        q.set('blue', 1)
        assert q.load == 5/float(12)


if __name__ == '__main__':
    unittest.main()
