from task1.LinkedListBase import LinkedListBase


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

    def extend(self, b_list):
        if not isinstance(b_list, BidirectionalLinkedList):
            raise TypeError('The input must be a LinkedList!')

        b_list._head.prev = self._tail
        self._tail.next = b_list._head
        self._tail = b_list._tail
        self._len += b_list.length


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


    l = BidirectionalLinkedList()
    test_list(l)
