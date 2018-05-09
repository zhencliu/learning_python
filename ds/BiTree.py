#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    ds.BiTree

    An implementation for binary tree.
'''
import pdb

class TreeNode:
    def __init__(self, value = None):
        self.value = value
        self.left  = None
        self.right = None
        self.parent= None

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
        l = [self.root]


class BSTree(BiTree):
    '''Binary search tree.'''
    def __init__(self):
        super().__init__()

    def insert(self, value):
        new = TreeNode(value)

        if self.empty():
            self._root = new
        else:
            self._insert(self._root, new)
        
        self._count += 1

    def _insert(self, node, new):
        if node is None:
            return new
        else:
            if new.value < node.value:
                node.left  = self._insert(node.left, new)
            else:
                node.right = self._insert(node.right, new)
            
            return node
     
    def create(self, iterator):
        for val in iterator:
            self.insert(val)

if __name__ == '__main__':
    import random

    t = BSTree();
    t.create(random.sample(range(100), 10))
    t.inorder()

