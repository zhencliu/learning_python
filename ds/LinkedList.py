#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, val):
        self.value = val
        self.next = self.prev = None

class SLinkedList(object):
    def __init__(self):
        self.head_tail = Node(0)

    def __len__(self):
        return self.head_tail.value

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

        return node

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

        return node

    def print_list(self):
        node = self.head_tail.next
        while (node):
            print(node.value)
            node = node.next

if __name__ == '__main__':
    s = SLinkedList();

    for i in range(1, 6):
        s.insert_head(i)

    for i in range(6, 11):
        s.insert_tail(i)

    s.print_list()
