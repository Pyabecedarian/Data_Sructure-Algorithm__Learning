"""

"""
from task1.LinkedList import LinkedList


class HashTable(object):

    def __init__(self, size=13):
        self._size = size
        self._slots = [LinkedList() for _ in range(self._size)]
        self._items = [LinkedList() for _ in range(self._size)]

    def __str__(self):
        s = ''
        for i, k in enumerate(self._slots):
            s += '| -> %s  ' % i
            if k.is_empty():
                s += '\n'
                continue
            else:
                s += str(self._items[i]) + '\n'
        return '\n' + s

    def __setitem__(self, key, value):
        hashed_key = self._hash(key)
        i = self._slots[hashed_key].search(key)
        if i != -1:
            self._items[hashed_key][i] = value
        else:
            self._slots[hashed_key].append(key)
            self._items[hashed_key].append(value)

    def __getitem__(self, key):
        hashed_key = self._hash(key)
        i = self._slots[hashed_key].search(key)
        if i != -1:
            return self._items[hashed_key][i]
        else:
            raise KeyError('No such key in HashTable:', key)

    def __delitem__(self, key):
        hashed_key = self._hash(key)
        i = self._slots[hashed_key].search(key)
        if i != -1:
            return
        else:
            self._slots[hashed_key].remove(i)
            self._items[hashed_key].remove(i)

    def pop(self, key):
        hashed_key = self._hash(key)
        i = self._slots[hashed_key].search(key)
        if i is None:
            return
        else:
            self._slots[hashed_key].remove(i)
            return self._items[hashed_key].remove(i)

    def put(self, key, value):
        self[key] = value

    def _hash(self, key):
        if isinstance(key, str):
            s = 0
            for c in key:
                s += ord(c)
            key = s
        return key % self._size


if __name__ == '__main__':
    h = HashTable(size=3)

    # Add some value
    h[1] = 1
    h[2] = 2
    h[3] = 3
    print(h)

    h[1] = 11
    print(h)