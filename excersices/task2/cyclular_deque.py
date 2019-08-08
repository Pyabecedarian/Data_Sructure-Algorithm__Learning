from task1.LinkedList import LinkedList


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._items = LinkedList()
        self._size = k

    def __str__(self):
        return str(self._items)

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self._items) < self._size:
            self._items.prepend(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self._items) < self._size:
            self._items.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self._items) > 0:
            self._items.del_first()
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self._items) > 0:
            self._items.del_last()
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self._items[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self._items[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        print(self._items._head)
        return self._items.is_empty()

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self._items) == self._size


if __name__ == '__main__':
    obj = MyCircularDeque(4)
    print('InsertFront:', obj.insertFront(0))
    print('After InsertFront:', obj)

    print('InsertLast:', obj.insertLast(3))
    print('After InsertLast:', obj)

    print('GetFront:', obj.getFront())
    print('GetLast:', obj.getRear())

    print('IsEmpty:', obj.isEmpty())
    print('IsFull:', obj.isFull())

    print('DeleteFront:', obj.deleteFront())
    print('After deleteFront:', obj)

    print('DeleteLast:', obj.deleteLast())
    print('After deleteLast:', obj)

    print('IsEmpty:', obj.isEmpty())
    print('IsFull:', obj.isFull())
    """
    InsertFront: True
    After InsertFront: [ 0 ]
    InsertLast: True
    After InsertLast: [ 0 3 ]
    GetFront: 0
    GetLast: 3
    0
    IsEmpty: False
    IsFull: False
    DeleteFront: True
    After deleteFront: [ 3 ]
    DeleteLast: True
    After deleteLast: [ ]
    None
    IsEmpty: True
    IsFull: False
    """

