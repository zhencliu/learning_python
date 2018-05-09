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
            head_tail.next -> head node -> node ... -> tail node <- head_tail.prev
            head_tail.value -> the count of nodes in the list.
    ''' 
    def __init__(self):
        self.head_tail = Node(0)

    def __len__(self):
        return self.head_tail.value

    def __str__(self):
        l = []

        for value in self:
            l.append(str(value))
        
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
           
    def __setitem__(self, index, value):
        '''Make a linked list accessed by index, i.e. list[index] = value
        '''
        if 0 <= index < self.head_tail.value:
            self._goto(index).value = value
        else:
            raise ValueError("out of space.")
    
    def __getitem__(self, index):
        '''Make a linked list accessed by index, i.e. list[index]
        '''
        if 0 <= index < self.head_tail.value:
            return self._goto(index).value
        else:
            return None
    
    def _goto(self, index):
        i = 0
        node = self.head_tail.next;

        while (i < index):
            node = node.next
            i += 1

        return node
                
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
        for value in self:
            print(value)

class DLinkedList(object):
    ''' A double linked list.
        head_tail is a node which identifies the head and tail node.
            head node.prev -> head_tail
            tail node.next -> head_tail

            head_tail.next<=>head node<=>node...<=>tail node<=>head_tail.prev
            head_tail.value -> the count of nodes in the list.
    ''' 
    def __init__(self):
        self.head_tail = Node(0)
        self.head_tail.next = self.head_tail.prev = self.head_tail

    def __len__(self):
        return self.head_tail.value

    def __str__(self):
        l = []

        for value in self:
            l.append(str(value))
        
        return 'Elem List: %s' %(' '.join(l))

    __repr__ = __str__
     
    def __iter__(self):
        self.curr = self.head_tail.next
        return self
    
    def __next__(self):
        curr = self.curr

        if curr is self.head_tail:
            # Re-set the curr pointer to the head
            self.curr = self.head_tail.next
            raise StopIteration()

        self.curr = self.curr.next
        return curr.value
           
    def __setitem__(self, index, value):
        '''Make a linked list accessed by index, i.e. list[index] = value
        '''
        if 0 <= abs(index) < self.head_tail.value or index == -(self.head_tail.value):
            self._goto(index).value = value
        else:
            raise ValueError("out of space.")

    def __getitem__(self, index):
        '''Make a linked list accessed by index, i.e. list[index]
        '''
        if 0 <= abs(index) < self.head_tail.value or index == -(self.head_tail.value):
            return self._goto(index).value
        else:
            return None
    
    def _goto(self, index):
        node = None
        if index < 0:
            node = self.head_tail.prev;
            i = 1
            while i < abs(index):
                node = node.prev
                i += 1
        else:
            node = self.head_tail.next;
            i = 0
            while i < index:
                node = node.next
                i += 1

        return node

    def insert_head(self, value):
        node = Node(value)

        if self.head_tail.value == 0:
            self.head_tail.next = self.head_tail.prev = node
            node.next = self.head_tail
        else:
            node.next = self.head_tail.next
            self.head_tail.next.prev = node
            self.head_tail.next = node

        node.prev = self.head_tail
        self.head_tail.value += 1

    def insert_tail(self, value):
        node = Node(value)

        if self.head_tail.value == 0:
            self.head_tail.next = self.head_tail.prev = node
            node.prev = self.head_tail
        else:
            self.head_tail.prev.next = node
            node.prev = self.head_tail.prev
            self.head_tail.prev = node

        node.next = self.head_tail
        self.head_tail.value += 1

    def pop_head(self):
        node = self.head_tail.next
        self.head_tail.value -= 1

        if self.head_tail.value <= 0:
            # An empty list
            self.head_tail.next = self.head_tail.prev = self.head_tail
            self.head_tail.value = 0
        else:
            # Re-set the head
            self.head_tail.next = node.next
            node.next.prev = self.head_tail
        
        if node is not self.head_tail:
            return node.value
        else:
            return None

    def pop_tail(self):
        node = self.head_tail.prev
        self.head_tail.value -= 1

        if self.head_tail.value <= 0:
            # An empty list
            self.head_tail.next = self.head_tail.prev = self.head_tail
            self.head_tail.value = 0
        else:
            # Re-set the tail 
            self.head_tail.prev = node.prev
            node.prev.next = self.head_tail

        if node is not self.head_tail:
            return node.value
        else:
            return None

    def print_list(self):
        for value in self:
            print(value)

    def print_list_reverse(self):
        node = self.head_tail.prev
        while node is not self.head_tail:
            print(node.value)
            node = node.prev

if __name__ == '__main__':
    sl = SLinkedList();
    dl = DLinkedList();

    for s in sl,dl:
        # Pop an empty list
        print("Testing linked list")
        print("pop head: %s" %s.pop_head())
        print("pop tail: %s" %s.pop_tail())
    
        # Insert head
        for i in range(1, 6):
            s.insert_head(i)
    
        # Insert tail 
        for i in range(6, 11):
            s.insert_tail(i)
    
        print("index 9: %s" % s[9])
        print("index 0: %s" % s[0])
        print("index -1: %s" % s[-1])
        print("index -10: %s" % s[-10])
        print("index 100: %s" % s[100])
    
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
    
        # Call __setitem__ and __getitem__
        print("getitem: %s" %s[len(s) - 1])
        s[len(s) - 1] = None
        print("after setitem: %s" %s[len(s) - 1])
    
        #s.print_list_reverse()
