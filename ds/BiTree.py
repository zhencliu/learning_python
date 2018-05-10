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

    @property 
    def root(self):
        return self._root

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

    def print(self):
        from collections import deque

        q = deque()
        q.appendright(self.root)
        
        while not q.empty():
            node = q.popleft()
            print(node.value)

            if node.left is not None:
                q.appendright(node.left)
            
            if node.right is not None:
                q.appendright(node.right)

