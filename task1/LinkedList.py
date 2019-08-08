from task1.LinkedListBase import LinkedListBase


class LinkedList(LinkedListBase):
    """Class of LinkedList"""

    def __init__(self, *args, **kwargs):
        super(LinkedList, self).__init__()

        for elem in args:
            self.append(elem)

        if 'size' in kwargs:
            for i in range(kwargs['size']):
                self.append(0)

    def extend(self, b_list):
        if not isinstance(b_list, LinkedList):
            raise TypeError('The input must be a LinkedList!')

        self._tail.next = b_list._head
        self._tail = b_list._tail
        self._len += len(b_list)

    def insert(self, value, i):
        """Insert the element at index `i` while keeping the order of the structure unchanged. O(n)"""
        if i <= 0:
            return self.prepend(value)
        if i >= self._len:
            return self.append(value)

        p, n = self._head, 0
        while n + 1 < i:
            p = p.next
            n += 1

        p.next = self.Node(value, p.next)
        self._len += 1

    def del_first(self):
        """Delete the first element. O(1)"""
        if self._len == 0: return

        self._head = self._head.next
        self._len -= 1

    def del_last(self):
        """Delete the last element. O(n)"""
        if self.is_empty(): return

        p, n = self._head, 0
        while n + 1 < len(self) - 1:
            p = p.next
            n += 1

        from copy import deepcopy
        last = deepcopy(p.next)
        self._tail = p
        self._tail.next = None
        self._len -= 1
        return last

    def pop(self):
        """An alias of del_last()"""
        return self.del_last()

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
        """Merge the list `a` with another list `b` into a new list, keeping their original order, where
         a and b are both numerical ordered, and return this new merged list."""
        if not isinstance(b_list, LinkedList):
            raise TypeError('The input must be a LinkedList!')

        new_list = LinkedList()

        p1, p2 = self._head, b_list._head
        while True:
            if p1 is None:
                while p2 is not None:
                    new_list.append(p2.value)
                    p2 = p2.next
                break

            elif p2 is None:
                while p1 is not None:
                    new_list.append(p1.value)
                    p1 = p1.next
                break

            elif p1.value <= p2.value:
                new_list.append(p1.value)
                p1 = p1.next
            else:
                new_list.append(p2.value)
                p2 = p2.next

        return new_list


if __name__ == '__main__':
    def test_list(l):
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

        # get the middle node value in the list
        m = l.get_mid()
        print('value in middle is:', m)

        # pop
        print('Pop last value', l.pop())
        print('After pop:', l)


    # l = LinkedList()
    # l = CycleList()
    # l = BidirectionalLinkedList()
    # test_list(l)

    # l1 = LinkedList(5, 7, 9, 18, 20)
    # l2 = LinkedList(6, 10, 21, 30)
    # print('l1:', l1)
    # print('l2:', l2)
    #
    # # merge l1 and l2
    # new_l = l1.merge(l2)
    # print('merged list:', new_l)
    # print('Whether l1 or l2 is changed:')
    # print('l1:', l1)
    # print('l2:', l2)

    # size
    l = LinkedList(size=4)
    print(l)
