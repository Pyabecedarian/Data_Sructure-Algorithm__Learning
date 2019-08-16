"""
Least Recently Used
"""
from task1.LinkedList import LinkedList
from task4.hash_table import HashTable


class LRU(object):
    def __init__(self, size=3):
        self._size = size
        self._cache = HashTable()
        self._keys = LinkedList()

    def __str__(self):
        return str(self._keys)

    def __setitem__(self, key, value):
        if len(self._keys) < self._size:
            self._keys.prepend(key)
            self._cache[key] = value
        else:
            k = self._keys.pop(key)
            if k is None:
                last_key = self._keys.pop()
                self._keys.prepend(key)
                self._cache.pop(last_key)
                self._cache[key] = value
            else:
                self._keys.prepend(key)
                self._cache[key] = value

    def __getitem__(self, key):
        return self._cache[key]


if __name__ == '__main__':
    lru = LRU()
    print(lru)

    # add some data
    lru['1st'] = 1
    lru['2nd'] = 2
    lru['3rd'] = 3
    print(lru)

    print('Continue')
    lru['4th'] = 4  # '1st' is removed
    print(lru)
    lru['5th'] = 5  # '2nd' is removed
    print(lru)

    # if operate on existed data
    lru['3rd'] = 33
    print(lru)
    print(lru['3rd'])
