#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    ds.LinkedList

    An implementation for both single and double linked list.
'''

class Node(object):
    ''' Node object has two pointers: prev->node before, next->node after '''
    def __init__(self, val):
        self.value = val
        self.next = self.prev = None

class SLinkedList(object):
    ''' A single linked list.
        head_tail is a node which identifies the head and tail node.
            head_tail.next -> the head
            head_tail.prev -> the tail
            head_tail.value -> the count of nodes in the list.
    ''' 
    def __init__(self):
        self.head_tail = Node(0)

    def __len__(self):
        return self.head_tail.value

    def __str__(self):
        node = self.head_tail.next
        l = []

        while (node):
            l.append(str(node.value))
            node = node.next
        
        return 'Elem List: %s' %(' '.join(l))

    __repr__ = __str__
     
    def __iter__(self):
        self.curr = self.head_tail.next
        return self
    
    def __next__(self):
        curr = self.curr

        if curr is None:
            # Re-set the curr pointer to the head
            self.curr = self.head_tail.next
            raise StopIteration()

        self.curr = self.curr.next
        return curr.value
           

    def insert_head(self, value):
        node = Node(value)

        if self.head_tail.value == 0:
            self.head_tail.next = self.head_tail.prev = node
        else:
            self.head_tail.next, node.next = node, self.head_tail.next

        self.head_tail.value += 1

    def insert_tail(self, value):
        node = Node(value)

        if self.head_tail.value == 0:
            self.head_tail.next = self.head_tail.prev = node
        else:
            self.head_tail.prev.next = node
            self.head_tail.prev = node

        self.head_tail.value += 1

    def find_prev(self, node):
        n = self.head_tail.next

        while n is not None and n.next is not node:
            n = n.next
        
        return n

    def pop_head(self):
        node = self.head_tail.next
        self.head_tail.value -= 1

        if self.head_tail.value <= 0:
            # An empty list
            self.head_tail.next = self.head_tail.prev = None
            self.head_tail.value = 0
        else:
            # Re-set the head
            self.head_tail.next = node.next
        
        if node:
            return node.value
        else:
            return None

    def pop_tail(self):
        node = self.head_tail.prev
        self.head_tail.value -= 1

        if self.head_tail.value <= 0:
            # An empty list
            self.head_tail.next = self.head_tail.prev = None
            self.head_tail.value = 0
        else:
            # Re-set the tail 
            self.head_tail.prev = self.find_prev(node)
            self.head_tail.prev.next = None

        if node:
            return node.value
        else:
            return None

    def print_list(self):
        node = self.head_tail.next

        while (node):
            print(node.value)
            node = node.next

if __name__ == '__main__':
    s = SLinkedList();

    # Pop an empty list
    print(s.pop_head())
    print(s.pop_tail())

    # Insert head
    for i in range(1, 6):
        s.insert_head(i)

    # Insert tail 
    for i in range(6, 11):
        s.insert_tail(i)

    # Call __str__()
    print(s)

    # Call __iter__() and __next__()
    for val in s:
        print("Iteration: %s" %val)

    # Pop head and pop tail
    print("pop tail: %s" %s.pop_tail())
    print("pop head: %s" %s.pop_head())
    s.print_list()

    # Call __len__()
    print("Length of the list: %d" %len(s))

    for val in s:
        print("Iteration: %s" %val)
