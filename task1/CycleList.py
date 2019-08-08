from task1.LinkedList import LinkedList


class CycleList(LinkedList):
    def __init__(self, *args):
        super(CycleList, self).__init__()

        for elem in args:
            self.append(elem)

    def prepend(self, value):
        super(CycleList, self).prepend(value)
        self._tail.next = self._head

    def append(self, value):
        super(CycleList, self).append(value)
        self._tail.next = self._head

    def del_first(self):
        super(CycleList, self).del_first()
        self._tail.next = self._head

    def del_last(self):
        super(CycleList, self).del_last()
        self._tail.next = self._head

    def reverse(self):
        self._tail.next = None
        super(CycleList, self).reverse()
        self._tail.next = self._head

    def extend(self, b_list):
        if not isinstance(b_list, CycleList):
            raise TypeError('The input must be a CycleList!')

        self._tail.next = b_list._head
        self._tail = b_list._tail
        self._tail.next = self._head
        self._len += len(b_list)


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



    l = CycleList()
    # l = BidirectionalLinkedList()
    test_list(l)
