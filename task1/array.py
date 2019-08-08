"""
Array： dynamic scaling array
"""
import ctypes

class Array(object):
    def __init__(self, size):
        self._size = size
        self._values = []

    def add(self, value):
        if len(self._values) >= self._size:
            raise ValueError('The list is full, you cannot add any value!')
        self._values.append(value)

    def delete(self, value):
        try:
            self._values.remove(value)
        except ValueError:
            pass

    def __str__(self):
        return '[ ' + ''.join(str(i) + ' ' for i in self._values) + ']'


if __name__ == '__main__':
    a = Array(4)
    a.add(2)
    a.add(19)
    a.add(31)
    a.add(190)
    print(a)
    a.delete(19)
    print(a)
