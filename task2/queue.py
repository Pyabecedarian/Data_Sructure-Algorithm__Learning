"""
A queue is an ordered collection of items where the addition of new items happens at one end,
called the “rear,” and the removal of existing items occurs at the other end, commonly called
the “front.” As an element enters the queue it starts at the rear and makes its way toward the
front, waiting until that time when it is the next element to be removed, aka. FIFO.

The queue operations are:
    > Queue(): creates a new queue that is empty. It needs no parameters and returns an empty queue.
    > enqueue(item): adds a new item to the rear of the queue. It needs the item and returns nothing.
    > dequeue(): removes the front item from the queue. It needs no parameters and returns the item.
                The queue is modified.
    > isEmpty(): tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
    > size(): returns the number of items in the queue. It needs no parameters and returns an integer.
"""
from task1.LinkedList import LinkedList


class Queue(object):
    """Implement stack using LinkedList"""
    def __init__(self):
        self._items = LinkedList()

    def __str__(self):
        return '[ ' + ' '.join(str(i) for i in self._items) + ' ]'

    def enqueue(self, item):
        self._items.prepend(item)

    def dequeue(self):
        return self._items.pop()

    def isEmpty(self):
        return self._items.is_empty()

    @property
    def size(self):
        return len(self._items)


if __name__ == '__main__':
    q = Queue()
    print('S is empty:', q.isEmpty())
    print('Enqueue some values:')
    q.enqueue(2)
    q.enqueue(4)
    q.enqueue('Hello')
    print('After enqueue:', q)
    print('Size:', q.size)
    q.enqueue(0.98)
    print('Now queue is:', q)
    print('Dequeue a value:', q.dequeue())
    print('Dequeue a value:', q.dequeue())
    print('After Dequeue:', q)

    """
    S is empty: True
    Enqueue some values:
    After enqueue: [ Hello 4 2 ]
    Size: 3
    Now queue is: [ 0.98 Hello 4 2 ]
    Dequeue a value: 2
    Dequeue a value: 4
    After Dequeue: [ 0.98 Hello ]
    """