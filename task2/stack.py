"""
A stack is structured, as described above, as an ordered collection of items
where items are added to and removed from the end called the “top.” Stacks are
ordered LIFO.

The stack operations are given below:

    > Stack(): creates a new stack that is empty. It needs no parameters and returns an empty stack.
    > push(item): adds a new item to the top of the stack. It needs the item and returns nothing.
    > pop(): removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
    > peek(): returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
    > isEmpty(): tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
    > size(): returns the number of items on the stack. It needs no parameters and returns an integer.
"""
from task1.LinkedList import LinkedList


class Stack(object):
    """Implement stack using LinkedList"""

    def __init__(self):
        self._items = LinkedList()

    def __str__(self):
        return '[ ' + ' '.join(str(i) for i in self._items) + ' ]'

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def isEmpty(self):
        return self._items.is_empty()

    @property
    def size(self):
        return len(self._items)


if __name__ == '__main__':
    s = Stack()
    print('S is empty:', s.isEmpty())
    print('Put some values:')
    s.push(2)
    s.push(4)
    print('After push:', s)
    print('Size:', s.size)
    print('Now stack is:', s)
    print('Pop a value:', s.pop())
    print('Pop a value:', s.pop())
    print('After pop:', s)
    """
    S is empty: True
    Put some values:
    After push: [ 2 4 Hello ]
    Size: 3
    Now stack is: [ 2 4 Hello 0.98 ]
    Pop a value: 0.98
    Pop a value: Hello
    After pop: [ 2 4 ]
    """
