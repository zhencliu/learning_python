#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    ds.BiTree

    An implementation for binary tree.
'''
from TreeNode import TreeNode

class BiTree(object):
    ''' A binary tree implementation.
    ''' 
    def __init__(self):
        self._root  = None
        self._count = 0

    def height(self, T):
        return T._height if T is not None else -1

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, cnt):
        self._count = cnt

    @property 
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        self._root = node

    def __len__(self):
        return self._count

    def empty(self):
        return self._count == 0

    def _preorder(self, node):
        if node is not None:
            print(node.value)
            self._preorder(node.left)
            self._preorder(node.right)

    def preorder(self):
        self._preorder(self.root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.value)
            self._inorder(node.right)

    def inorder(self):
        self._inorder(self.root)

    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.value)
    
    def postorder(self):
        self._postorder(self.root)

    def topdown(self):
        from collections import deque

        q = deque()
        q.append(self.root)
        cnt_current = 1
        cnt_next = 0
        list_current = []
        result = []
        
        while len(q) > 0:
            node = q.popleft()
            cnt_current -= 1
            list_current.append(node.value)

            if node.left is not None:
                q.append(node.left)
                cnt_next += 1
            
            if node.right is not None:
                q.append(node.right)
                cnt_next += 1

            if cnt_current == 0:
                cnt_current = cnt_next
                cnt_next = 0
                result.append(list_current)
                list_current = []

        return result

    def _clear(self, T):
        if T is not None:
            self._clear(T.left)
            self._clear(T.right)
            del T

    def clear(self):
        self._clear(self.root)
        #self.root = None
