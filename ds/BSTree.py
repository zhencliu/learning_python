#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    ds.BSTree

    An implementation for binary search tree.
'''
from TreeNode import TreeNode
from BiTree import BiTree

class BSTree(BiTree):
    '''Binary search tree.'''
    def __init__(self):
        super().__init__()

    def _insert(self, node, new):
        if node is None:
            return new
        else:
            if new.value < node.value:
                node.left  = self._insert(node.left, new)
            elif new.value == node.value:
                node.ref = node.ref + 1
            else:
                node.right = self._insert(node.right, new)
            
            return node
     
    def insert(self, value):
        new = TreeNode(value)
        new.ref = 1

        if self.empty():
            self._root = new
        else:
            self._insert(self._root, new)
        
        self._count += 1

    def delete(self, value):
        if self.empty():
            self._root = new
        else:
            self._insert(self._root, new)
        
        self._count += 1

    def create(self, iterator):
        for val in iterator:
            self.insert(val)

if __name__ == '__main__':
    import random

    t = BSTree();
    t.create(random.sample(range(100), 10))
    print("Inorder:")
    t.inorder()
    print("Preorder:")
    t.preorder()
    print("Postorder:")
    t.postorder()

    res = t.topdown()
    print("topdown: %s" %res)
    print("bottomup: %s" %res[::-1])

