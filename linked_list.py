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
    class Node(object):
        """Meta class for linked structure"""

        def __init__(self, value, __next__):
            self.value = value
            self.next = __next__

    def __init__(self):
        self._len = 0
        self._head = None
        self._tail = None

    def __len__(self):
        """Support python built-in len() function, return the length of the list. O(1)"""
        return self._len

    @property
    def length(self):
        """Return the length of the list. O(1)"""
        return self._len

    def __str__(self):
        s = '['
        p = self._head
        while p is not None:
            s += ' ' + str(p.value)
            p = p.next
        return s + ' ]'


class LinkedList(LinkedListBase):
    """Implementation of LinkedList__single direction"""

    def __init__(self, *args):
        super(LinkedList, self).__init__()

        for elem in args:
            self.append(elem)

    def is_empty(self):
        """Return True if List is empty.  O(1)"""
        return self._head is None

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
        if i >= self._len - 1: return self.append(elem)

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

    def search(self, elem):
        """Search a element whether or not in the List and return it's index. If not in the list, return -1. O(n)"""
        p, n = self._head, 0
        while p is not None:
            if p.value == elem: return n
            p = p.next
            n += 1
        return -1

    def for_each(self, func, *args, **kwargs):
        """Apply each element in the list to a function. O(n)"""
        p = self._head
        while p is not None:
            p.value = func(p.value, *args, **kwargs)
            p = p.next

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

    def get_mid(self):
        """Return the middle value of the list. O(n)"""
        p = self._head
        n = 0
        while n < self._len - 1:
            p = p.next
            n += 2
        return p.value


if __name__ == '__main__':
    def test_single_directional_list():
        l = LinkedList()

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
        print('Length of list:', len(l))
        l.insert('<start>', 0)  # insert as first element
        l.insert('<end>', 6)  # insert as last element
        l.insert('<mid>', 3),  # insert in middle
        print('After insert:', l)

        # del the first element
        l.del_first()
        print('After del first:', l)

        # del the last element
        l.del_last()
        print('After del last:', l)

        # remove a element in middle
        l.remove(2)
        print('After remove:', l)

        # search the index of  value `6` in l
        print('the index of value 8 in l is:', l.search(6))

        # squared each element in l
        l.for_each(lambda x: x ** 2)
        print('After squared:', l)

        # use bracket for indexing and signing
        l[0] = 'start'
        print('After signing value:', l)
        print('Indexing at position 6:', l[6])

        # reverse a list
        l.reverse()
        print('After reverse:', l)

        # merge two lists
        l2 = LinkedList(1, 2, 3)
        print('New list to be merged:', l2)
        l.merge(l2)
        print('After merging l2:', l)
        print('After merging, total length is:', l.length)

        # get the value in middle of a list
        m = l.get_mid()
        print('The value in middle of l is:', m)


    def test_cycle_list():
        pass
