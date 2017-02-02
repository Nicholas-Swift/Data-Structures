# A Hash Table

from linkedlist import LinkedList


class Set(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        # Best: Omega(1)
        # Worst: O(n) (init size)

        self.buckets = [LinkedList() for i in range(init_size)]
        self.entries = 0
        self.load = self.entries / len(self.buckets)
        self.max_load = 2/float(3)

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def __contains__(self, key):
        """Does it contain the item"""
        # Best: Omega(1)
        # Worst: O(n)

        bucket = self._bucket(key)

        for item in bucket:
            if key == item:
                return True
        return False

    def __iter__(self):
        """Iterate through the hash table"""
        # Best: Omega(1)
        # Worst: O(1)

        for bucket in self.buckets:
            if bucket:
                for item in bucket:
                    yield item

    def _update_entries(self, number_added):
        """Update the number of entries and update the load, resize if needed"""
        # Best: Omega(1)
        # Worst: O(1)

        self.entries += number_added
        self.load = self.entries / float(len(self.buckets))

        if self.load > self.max_load:
            self._resize_up()

    def _resize_up(self):
        """The load factor is greater than 0.75! Resize and Rehash! Resize and Rehash it all!"""
        # Best: Omega(n)
        # Worst: O(n)

        new_length = len(self.buckets)*2

        # Create new buckets list, recalculate load with new_length
        new_buckets = [LinkedList() for i in range(new_length)]
        self.load = self.entries / float(new_length)

        # Iterate through current items and add to new buckets
        for item in self.__iter__():
            index = hash(item) % new_length
            new_buckets[index].append(item)

        self.buckets = new_buckets
        return

    def _resize_down(self):
        """Resize down! There are too many buckets and too little entries. Resize and Rehash!"""
        # Best: Omega(n)
        # Worst: O(n)

        new_length = self.entries * 2

        # Create new buckets list, recalculate load with new_length
        new_buckets = [LinkedList() for i in range(new_length)]
        self.load = self.entries / float(new_length)

        # Iterate through current items and add to new buckets
        for item in self.__iter__():
            index = hash(item) % new_length
            new_buckets[index].append(item)

        self.buckets = new_buckets
        return

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        # Best: Omega(1)
        # Worst: O(1)

        return hash(key) % len(self.buckets)

    def _bucket(self, key):
        """Return the bucket where the given key would be stored"""
        # Best: Omega(1)
        # Worst: O(1)

        index = self._bucket_index(key)
        return self.buckets[index]

    def length(self):
        """Return the length of this hash table"""
        # Best: Omega(1)
        # Worst: O(1)

        return self.entries

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # Best: Omega(1)
        # Worst: O(n) (number of items in bucket)

        bucket = self._bucket(key)
        for item_key, item_value in bucket:
            if key == item_key:
                return True
        return False

    def add(self, item):
        """Insert the given item to the set"""
        # Best: Omega(1)
        # Worst: Omega(1)

        bucket = self._bucket(item)
        bucket_item = bucket.find(lambda x: x == item)
        if bucket_item is None:
            bucket.append(item)
            self._update_entries(1)

    def remove(self, item):
        """Delete the given item from this hash table, or raise KeyError"""
        # Best: Omega(1)
        # Worst: O(n)

        bucket = self._bucket(item)
        bucket_item = bucket.find(lambda x: x == item)
        if bucket_item is not None:
            bucket.delete(item)
            self._update_entries(-1)
            return
        else:
            raise KeyError('Item is not in HashTable')

    def items(self):
        """Return a list of all items in this hash table"""
        # Best: Omega(n) (number of items in hash table)
        # Worst: O(n)
        items = []
        for item in self.__iter__():
            items.append(item)
        return items

    def shrink():
        """Let user shrink the hash table to fit"""
        # Best: Omega(n)
        # Worst: O(n)

        self._resize_down()
        return

    def clear(self):
        """Empty the Linked List"""
        # Best: Omega(1)
        # Worst: O(n) (number of buckets)

        for i, bucket in enumerate(self.buckets):
            if bucket:
                self.buckets[i] = LinkedList()
        self.entries = 0
        self.load = 0


def test_hash_table():
    ht = HashTable()
    ht.set('1', 1)
    ht.set('2', 1)
    ht.set('3', 1)

    for i in ht.buckets:
        print(i)


if __name__ == '__main__':
    test_hash_table()

