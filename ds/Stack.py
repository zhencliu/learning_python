#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    ds.Stack

    An implementation for stack using single linked list
'''
from LinkedList import SLinkedList

class Stack(SLinkedList):
    ''' A stack implemented by a SLinkedList.
    ''' 
    def __init__(self):
        super().__init__()

    def push(self, value):
        self.insert_tail(value)

    def top(self):
        node = self.head_tail.prev

        if node:
            return node.value
        else:
            return None

    def pop(self):
        return self.pop_tail()


if __name__ == '__main__':
    s = Stack();

    # Pop an empty list
    print(s.top())
    print(s.pop())

    # Insert head
    for i in range(1, 6):
        s.push(i)

    # Call __str__()
    print(s)

    # Call __iter__() and __next__()
    for val in s:
        print("Iteration: %s" %val)

    # Pop head and pop tail
    print("top: %s" %s.top())
    print("pop: %s" %s.pop())

    # Call __len__()
    print("Length of the list: %d" %len(s))

    print("pop: %s" %s.pop())
    print("pop: %s" %s.pop())
    print("pop: %s" %s.pop())
    print("pop: %s" %s.pop())
    print("pop: %s" %s.pop())
    print("Length of the list: %d" %len(s))
