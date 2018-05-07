#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    ds.Stack

    An implementation for stack using single linked list
'''
from LinkedList import SLinkedList

class Queue(SLinkedList):
    ''' A queue implemented by a SLinkedList.
    ''' 
    def __init__(self):
        super().__init__()

    def enqueue(self, value):
        self.insert_tail(value)

    def top(self):
        node = self.head_tail.next

        if node:
            return node.value
        else:
            return None

    def dequeue(self):
        return self.pop_head()


if __name__ == '__main__':
    s = Queue();

    # Pop an empty list
    print(s.top())
    print(s.dequeue())

    # Insert head
    for i in range(1, 6):
        s.enqueue(i)

    # Call __str__()
    print(s)

    # Call __iter__() and __next__()
    for val in s:
        print("Iteration: %s" %val)

    # Pop head and pop tail
    print("top: %s" %s.top())

    # Call __len__()
    print("Length of the list: %d" %len(s))

    print("pop: %s" %s.dequeue())
    print("pop: %s" %s.dequeue())
    print("pop: %s" %s.dequeue())
    print("pop: %s" %s.dequeue())
    print("pop: %s" %s.dequeue())
    print("Length of the list: %d" %len(s))
