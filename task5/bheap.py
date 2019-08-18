class BinHeap(object):
    def __init__(self):
        self.size = 0
        self.heapList = [0]

    def __str__(self):
        return '[ ' + ' '.join(str(i) for i in self.heapList[1:]) + ' ]'

    def _percolateUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i //= 2

    def _percolateDown(self, i):
        while i * 2 <= self.size:
            minC_idx = self._getMinChildIndex(i)
            if self.heapList[i] > self.heapList[minC_idx]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minC_idx]
                self.heapList[minC_idx] = tmp
            i = minC_idx

    def _getMinChildIndex(self, i):
        if i * 2 == self.size:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, value):
        self.heapList.append(value)
        self.size += 1
        self._percolateUp(self.size)

    def delMin(self):
        vmin = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.heapList.pop()
        self.size -= 1
        self._percolateDown(1)
        return vmin

    def build_from_list(self, aList):
        """
        One can build a heap by just inserting an item one at a time.
        This process is at O(log_n) ops. Since inserting an item in
        middle of a list will cause O(n) ops, thus the whole process
        will finally cost O(n*log_n).

        However if start building a heap with an entire list, that will
        end up with O(n) ops.
        """
        i = len(aList) // 2
        self.heapList = [0] + aList
        self.size = len(aList)
        while i > 0:
            self._percolateDown(i)
            i -= 1


if __name__ == '__main__':
    bh = BinHeap()
    print(bh)

    bh.insert(17)
    bh.insert(14)
    bh.insert(9)
    bh.insert(5)

    print(bh)

    bh = BinHeap()
    bh.build_from_list([14, 9, 17, 5, 18, 21, 3])
    print(bh)

    bh.delMin()
    print('del Min:', bh)
    bh.delMin()
    print('del Min:', bh)
    bh.delMin()
    print('del Min:', bh)
