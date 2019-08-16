"""
Linked List:
    A `list`(unordered list) is a collection of items where each item holds a
    relative position w.r.t the others.

Some abstract methods:
    > LinkedList(): Initialization Method, creates a new list;
    > is_empty(): Whether a list is empty or not;
    > len(): Return the length of the list;
    > prepend(elem): Prepend as the first element in a list;
    > append(elem): Append as the last element in a list;
    > insert(elem, i): Insert an element in position `i` while hold the order unchanged;
    > del_first(): Delete the first element in a list;
    > del_last(): Delete the last element in a list;
    > remove(i): Delete the element in position `i`;
    > search(elem): Search the element in a list and return it's position. If not such
                    element, return -1;
    > for_each(op_func): Apply operation function to all element in list;
    > reverse(): Reverse the order of the list;
    > merge(b_list): Merge with another list `b`;
    > get_mid(): Get the value in the middle of the list
"""


class LinkedListBase(object):
    """Base class for LinkedList family"""

    class Node(object):
        """Meta class for linked structure"""

        def __init__(self, value, __next__=None):
            self.value = value
            self.next = __next__

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self._len = 0
        self._head = None
        self._tail = None

    def __str__(self):
        if self.is_empty(): return '[ ]'

        p, n, s = self._head, 0, ''
        while n < self._len:
            s += ' ' + str(p.value)
            p = p.next
            n += 1

        return '[' + s + ' ]'

    def __len__(self):
        return self._len

    def __index__(self, i):
        return i if i >= 0 else len(self) + i

    def __setitem__(self, i, value):
        i = self.__index__(i)
        if i < 0 or i >= self._len or self.is_empty():
            raise IndexError('Indexing assignment out of bound!')

        p, n = self._head, 0
        while n != i:
            p = p.next
            n += 1
        p.value = value

    def __getitem__(self, i):
        i = self.__index__(i)
        if i < 0 or i >= self._len or self.is_empty():
            raise IndexError('Indexing list out of bound!')

        p, n = self._head, 0
        while n != i:
            p = p.next
            n += 1
        return p.value

    def __iter__(self):
        self._n = -1
        return self

    def __next__(self):
        if self._n >= self._len - 1:
            self._n = -1
            raise StopIteration
        else:
            self._n += 1
            return self[self._n]

    @property
    def length(self):
        return self._len

    def is_empty(self):
        return self._head is None

    def get_mid(self):
        p, n = self._head, 0
        while n < self._len - 1:
            p = p.next
            n += 2
        return p.value

    def for_each(self, func, *args, **kwargs):
        p, n = self._head, 0
        while n < self._len:
            p.value = func(p.value, *args, **kwargs)
            p = p.next
            n += 1

    def search(self, elem):
        p, n = self._head, 0
        while n < self._len:
            if p.value == elem:
                return n
            p = p.next
            n += 1
        return -1

    def prepend(self, value):
        """Prepend the element as the first one in the list while keeping the order of structure. O(1)"""
        self._head = self.Node(value, self._head)
        self._len += 1

        if self._len == 1:
            self._tail = self._head

    def append(self, value):
        """Append the element at the rear of the list. O(1) """
        if self.is_empty():
            return self.prepend(value)

        self._tail.next = self.Node(value, None)
        self._tail = self._tail.next
        self._len += 1

    def extend(self, b_list):
        pass

    def insert(self, value, i):
        pass

    def del_first(self):
        pass

    def del_last(self):
        pass

    def remove(self, i):
        pass

    def reverse(self):
        pass

    def merge(self, b_list):
        pass

    def pop(self):
        pass
