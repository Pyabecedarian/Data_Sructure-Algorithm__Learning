"""
Array： dynamic scaling array
"""
import ctypes


class Array(object):
    _TYPES_ = {int: ctypes.c_int, float: ctypes.c_float, bool: ctypes.c_bool, str: ctypes.c_wchar}

    def __init__(self, type=int, size=1):
        self._size = size  # total size of array
        self._volume = 0   # current volume indicating how many numbers stored in the array
        self._type = self._cType(type)
        self._items = self._newArr()
        self._n = -1

    def __str__(self):
        return '[ ' + ' '.join(str(i) if not isinstance(i, str) else "'%s'" % i
                               for i in self._items[:self._volume]) + ' ]'

    def __iter__(self):
        return self

    def __next__(self):
        if self._n > self._volume - 2:
            self._n = -1
            raise StopIteration
        else:
            self._n += 1
            return self[self._n]

    def __index__(self, i):
        return i if i >= 0 else self._volume + i

    def __setitem__(self, i, value):
        i = self.__index__(i)
        if i >= self._size or i < 0:
            raise IndexError('Indexing assignment out of bound!')

        if i >= self._volume:
            self._volume = i + 1

        self._items[i] = value

    def __getitem__(self, i):
        i = self.__index__(i)
        if i >= self._size or i < 0:
            raise IndexError('Array index out of bound!')

        return self._items[i]

    def __len__(self):
        return self._volume

    def _cType(self, pyType):
        try:
            return self._TYPES_[pyType]
        except KeyError:
            raise TypeError('Incorrect Type. Array only supports {}.'.format(str(self._TYPES_.keys())))

    def _newArr(self):
        arr_type = self._type * self._size
        return arr_type()

    def _auto_scaling(self):
        # print('Array scaling...')
        self._size += self._size
        newArr = self._newArr()
        for i, value in enumerate(self._items):
            newArr[i] = value
        self._items = newArr

    def append(self, *values):
        for value in values:
            try:
                self[self._volume] = value
            except IndexError:
                self._auto_scaling()
                self[self._volume] = value

    def pop(self):
        out, self[-1] = self[-1], 0
        self._volume -= 1
        return out


if __name__ == '__main__':
    # create a Array of size 5
    a = Array(int, 6)

    # Assign value 2 at index 2
    a[2] = 2
    print(a)       # [ 0 0 2 ]
    print(len(a))  # 3

    # Append some values
    a.append(3)
    a.append(4, 5)
    print(a)       # [ 0 0 2 3 4 5 ]

    # Assign value 1 at index 1
    a[1] = 1
    print(a)       # [ 0 1 2 3 4 5 ]

    # Append more values
    a.append(6)    # [ 0 1 2 3 4 5 6 ]
    print(a)
    a.append(7, 8, 9)
    print(a)       # [ 0 1 2 3 4 5 6 7 8 9 ]
    a.append(10, 11, 12, 13, 14, 15)
    print(a)       # [ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ]

    # Pop last value
    a.pop()
    print(a)       #