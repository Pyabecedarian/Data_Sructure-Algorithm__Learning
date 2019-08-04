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

        def __init__(self, value, __next__):
            self.value = value
            self.next = __next__

    def __init__(self):
        self._len = 0
        self._head = None
        self._tail = None

    def __str__(self):
        s = '['
        p = self._head
        while p is not None:
            s += ' ' + str(p.value)
            p = p.next
        return s + ' ]'

    def __len__(self):
        """Support python built-in len() function, return the length of the list. O(1)"""
        return self._len

    @property
    def length(self):
        """Return the length of the list. O(1)"""
        return self._len

    def is_empty(self):
        """Return True if List is empty.  O(1)"""
        return self._head is None

    def get_mid(self):
        """Return the middle value of the list. O(n)"""
        p = self._head
        n = 0
        while n < self._len - 1:
            p = p.next
            n += 2
        return p.value

    def for_each(self, func, *args, **kwargs):
        """Apply each element in the list to a function. O(n)"""
        p = self._head
        while p is not None:
            p.value = func(p.value, *args, **kwargs)
            p = p.next

    def search(self, elem):
        """Search a element whether or not in the List and return it's index. If not in the list, return -1. O(n)"""
        p, n = self._head, 0
        while p is not None:
            if p.value == elem: return n
            p = p.next
            n += 1
        return -1


class LinkedList(LinkedListBase):
    """Implementation of LinkedList__single direction"""

    def __init__(self, *args):
        super(LinkedList, self).__init__()

        for elem in args:
            self.append(elem)

    def prepend(self, elem):
        """Prepend the element as the first one in the list while keeping the order of structure. O(1)"""
        self._head = self.Node(elem, self._head)
        self._len += 1

        if self._len == 1:
            self._tail = self._head

    def append(self, elem):
        """Append the element at the rear of the list. O(1) """
        if self._len == 0:
            return self.prepend(elem)

        self._tail.next = self.Node(elem, None)
        self._tail = self._tail.next
        self._len += 1

    def insert(self, elem, i):
        """Insert the element at index `i` while keeping the order of the structure unchanged. O(n)"""
        if i <= 0: return self.prepend(elem)
        if i >= self._len: return self.append(elem)

        p, n = self._head, 0
        while n + 1 < i:
            p = p.next
            n += 1

        p.next = self.Node(elem, p.next)
        self._len += 1

    def del_first(self):
        """Delete the first element. O(1)"""
        if self._len == 0: return
        self._head = self._head.next
        self._len -= 1

    def del_last(self):
        """Delete the last element. O(n)"""
        if self._len == 0: return

        p = self._head
        while p.next != self._tail:
            p = p.next

        self._tail = p
        self._tail.next = None
        self._len -= 1

    def remove(self, i):
        """Remove an element at index `i`.  O(n)"""
        if i <= 0: return self.del_first()
        if i >= self._len - 1: return self.del_last()

        p, n = self._head, 0
        while n + 1 < i:
            p = p.next
            n += 1
        p.next = p.next.next
        self._len -= 1

    def __setitem__(self, i, elem):
        if i <= 0: return self.prepend(elem)
        if i >= self._len - 1: return self.append(elem)
        return self.insert(elem, i)

    def __getitem__(self, i):
        if i >= self._len:
            raise KeyError('Indexing out of bound!')

        p, n = self._head, 0
        while n != i:
            p = p.next
            n += 1
        return p.value

    def reverse(self):
        """Reverse the order of List. O(n)"""
        self._tail = self._head

        p = None
        while self._head is not None:
            tmp = self._head
            self._head = tmp.next
            tmp.next = p
            p = tmp

        self._head = p

    def merge(self, b_list):
        """Merge this list with another list `b` into a new list, keeping their original order."""
        if not isinstance(b_list, LinkedList):
            raise TypeError('The input must be a LinkedList!')

        self._tail.next = b_list._head
        self._tail = b_list._tail
        self._len += len(b_list)


class CycleList(LinkedListBase):
    def __init__(self, *args):
        super(CycleList, self).__init__()

        for elem in args:
            self.append(elem)

    def __str__(self):
        s = '['
        p = self._head
        while True:
            s += ' ' + str(p.value)
            if p == self._tail: break
            p = p.next
        return s + ' ]'

    def prepend(self, elem):
        self._head = self.Node(elem, self._head)
        self._len += 1

        if self._len == 1:
            self._tail = self._head
            self._tail.next = self._head

    def append(self, elem):
        if self.length == 0:
            return self.prepend(elem)

        self._tail.next = self.Node(elem, self._head)
        self._tail = self._tail.next
        self._len += 1

    def insert(self, elem, i):
        if i <= 0: return self.prepend(elem)
        if i >= self._len: return self.append(elem)

        p, n = self._head, 0
        while True:
            if n + 1 == i:
                p.next = self.Node(elem, p.next)
                self._len += 1
                break
            p = p.next
            n += 1

    def del_first(self):
        if self._len == 0: return
        self._head = self._head.next
        self._tail.next = self._head
        self._len -= 1

    def del_last(self):
        if self._len == 0: return

        p = self._head
        while p.next != self._tail:
            p = p.next

        self._tail = p
        self._tail.next = self._head
        self._len -= 1

    def remove(self, i):
        if i <= 0: return self.del_first()
        if i >= self._len - 1: return self.del_last()

        p, n = self._head, 0
        while n + 1 < i:
            p = p.next
            n += 1

        p.next = p.next.next
        self._len -= 1

    def search(self, elem):
        p, n = self._head, 0
        while n < self._len:
            if p.value == elem:
                return n
            p = p.next
            n += 1
        return -1

    def for_each(self, func, *args, **kwargs):
        p = self._head
        while True:
            p.value = func(p.value, *args, **kwargs)
            if p == self._tail: break
            p = p.next

    def reverse(self):
        p = self._tail
        self._tail = self._head

        while True:
            tmp = self._head
            self._head = tmp.next
            tmp.next = p
            p = tmp
            if self._head == self._tail: break

        self._head = p

    def merge(self, b_list):
        if not isinstance(b_list, CycleList):
            raise TypeError('The input must be a LinkedList!')

        self._tail.next = b_list._head
        self._tail = b_list._tail
        self._tail.next = self._head
        self._len += len(b_list)


class BidirectionalLinkedList(LinkedListBase):
    class Node(LinkedListBase.Node):
        def __init__(self, value, __prev__, __next__):
            super().__init__(value, __next__)
            self.prev = __prev__

            if __prev__ is not None:
                __prev__.next = self

            if __next__ is not None:
                __next__.prev = self

    def __init__(self, *args):
        super(BidirectionalLinkedList, self).__init__()

        for elem in args:
            self.append(elem)

    def prepend(self, elem):
        self._head = self.Node(elem, None, self._head)
        self._len += 1
        if self._len == 1: self._tail = self._head

    def append(self, elem):
        if self._len == 0: return self.prepend(elem)
        self._tail = self.Node(elem, self._tail, None)
        self._len += 1

    def insert(self, elem, i):
        if i <= 0: return self.prepend(elem)
        if i >= self._len: return self.append(elem)

        p, n = self._head, 0
        while n + 1 < i:
            p = p.next
            n += 1

        p.next = self.Node(elem, p, p.next)
        self._len += 1

    def del_first(self):
        if self._len == 0: return
        self._head = self._head.next
        self._head.prev = None
        self._len -= 1

    def del_last(self):
        if self._len == 0: return
        self._tail = self._tail.prev
        self._tail.next = None
        self._len -= 1

    def remove(self, i):
        if i <= 0: return self.del_first()
        if i >= self._len - 1: self.del_last()

        p, n = self._head, 0
        while n + 1 < i:
            p = p.next
            n += 1

        p.next = p.next.next
        p.next.next.prev = p
        self._len -= 1

    def reverse(self):
        self._tail = self._head
        p = None
        while self._head is not None:
            tmp = self._head
            self._head = self._head.next
            tmp.next = p
            tmp.prev = self._head
            p = tmp
        self._head = p
        self._head.prev = None

    def merge(self, b_list):
        if not isinstance(b_list, BidirectionalLinkedList):
            raise TypeError('The input must be a LinkedList!')

        b_list._head.prev = self._tail
        self._tail.next = b_list._head
        self._tail = b_list._tail
        self._len += b_list.length


if __name__ == '__main__':
    def test_list(l):
        l = BidirectionalLinkedList()

        # prepend some elements
        l.prepend(3)
        l.prepend(2)
        l.prepend(1)
        print('After prepend:', l)

        # append some elements
        l.append(4)
        l.append(5)
        l.append(6)
        print('After append:', l)

        # insert some elements
        l.insert('start', 0)
        l.insert('end', len(l))
        l.insert('mid', 3)
        print('After insert:', l)

        # delete first element
        l.del_first()
        print('After delete first:', l)

        # delete last element
        l.del_last()
        print('After delete last:', l)

        # remove element at index `i`
        l.remove(2)
        print('After remove element at position `2`:', l)

        # search the index of value 6
        print('index is:', l.search(6))

        # squared list
        l.for_each(lambda x: x ** 2)
        print('Squared list:', l)

        # reverse list
        l.reverse()
        print('After reverse:', l)
        l.reverse()
        print('After reverse:', l)

        # merge with another cycle list b
        l2 = BidirectionalLinkedList(1, 2, 3)
        print('l2:', l2)
        l.merge(l2)
        print('After merge:', l)

        # get the middle node value in the list
        m = l.get_mid()
        print('value in middle is:', m)


    l = BidirectionalLinkedList()
    test_list(l)
