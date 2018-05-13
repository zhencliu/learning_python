#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    ds.AVLTree

    An implementation for AVL tree.
'''
from TreeNode import TreeNode
from BSTree import BSTree

class AVLTree(BSTree):
    '''AVL tree.'''
    def __init__(self):
        super().__init__()

    '''left-left
              T               q
             / \            /   \
            q   Tr  =>     ql    T
           / \            / \   / \
          ql   qr        n   n qr Tr
         / \
        n   n
    '''
    def rotate_right_single(self, T):
        q = T.left
        T.left = q.right
        q.right = T

        # bottom up height ajustment
        T.height = max(self.height(T.left), self.height(T.right)) + 1
        q.height = max(self.height(q.left), self.height(q.right)) + 1

        return q

    ''' right-right
              T               q
             / \            /   \
            Tl  q  =>      T     qr
               / \        / \    / \
              ql  qr     Tl  ql n   n
                  / \
                 n   n
    '''
    def rotate_left_single(self, T):
        q = T.right
        T.right = q.left
        q.left = T

        T.height = max(self.height(T.left), self.height(T.right)) + 1
        q.height = max(self.height(q.left), self.height(q.right)) + 1

        return q

    '''left-right
              T             T              qr
             / \           / \            /   \
            q   Tr  =>    qr  Tr  =>     q     T
           / \           / \            / \   / \
          ql  qr        q   n2         ql n1 n2 Tr 
             / \       / \
            n1  n2    ql  n1
    '''
    def rotate_right_double(self, T):
        T.left = self.rotate_left_single(T.left)
        return self.rotate_right_single(T)

    '''right-left
              T             T               ql
             / \           / \            /   \
            Tl  q   =>    Tl  ql   =>    T     q
               / \            / \       / \   / \
              ql  qr         n1  q     Tl  n1 n2 qr
             / \                / \
            n1  n2             n2  qr
    '''
    def rotate_left_double(self, T):
        T.right = self.rotate_right_single(T.right)
        return self.rotate_left_single(T)

    def _insert_recur(self, T, value):
        if T is None:
            new = TreeNode(value)
            return new
        elif value == T.value:
            T.ref += 1
        elif value < T.value:
            T.left = self._insert_recur(T.left, value)

            if self.height(T.left) - self.height(T.right) == 2:
                if value < T.left.value:
                    # insert node on the subtree T.left.left
                    T = self.rotate_right_single(T)
                else:
                    # insert node on the subtree T.left.right
                    T = self.rotate_right_double(T)
        else:
            T.right = self._insert_recur(T.right, value)
            
            if self.height(T.right) - self.height(T.left) == 2:
                if value > T.right.value:
                    # insert node on the subtree of T.right.right
                    T = self.rotate_left_single(T)
                else:
                    # insert node on the subtree of T.right.left
                    T = self.rotate_left_double(T)
        
        T.height = max(self.height(T.left), self.height(T.right)) + 1

        return T

    def _delete_recur(self, T, value):
        if T is None:
            return None
        elif value < T.value:
            T.left = self._delete_recur(T.left, value)
            
            if self.height(T.right) - self.height(T.left) == 2:
                # bug: height(T.right.right) >= height(T.right.left)
                #      single rotate left
                if self.height(T.right.right) < self.height(T.right.left):
                    T = self.rotate_left_double(T)
                else:
                    T = self.rotate_left_single(T)
        elif value > T.value:
            T.right = self._delete_recur(T.right, value)
            
            if self.height(T.left) - self.height(T.right) == 2:
                if self.height(T.left.left) < self.height(T.left.right):
                    T = self.rotate_right_double(T)
                else:
                    T = self.rotate_right_single(T)
        else:
            T.ref -= 1
            
            # remove the node from avl tree
            if T.ref == 0:
                if T.left is not None and T.right is not None:
                    minnode = self._min(T.right)
                    T.value, T.ref = minnode.value, minnode.ref
                    minnode.ref = 1 # to be deleted
                    T.right = self._delete_recur(T.right, T.value)
            
                    if self.height(T.left) - self.height(T.right) == 2:
                        if self.height(T.left.left) < self.height(T.left.right):
                            T = self.rotate_right_double(T)
                        else:
                            T = self.rotate_right_single(T)
                else:
                    T = T.left if T.left is not None else T.right

        if T is not None:
            T.height = max(self.height(T.left), self.height(T.right)) + 1

        return T

    def insert(self, value):
        self.root = self._insert_recur(self.root, value)
        self.count += 1

    def delete(self, value):
        self.root = self._delete_recur(self.root, value)        
        self.count -= 1


if __name__ == '__main__':
    import random

    t = AVLTree();
    t.create([3,2,1,4,5,6,7,16,15,14,13,12,11,10,8,9])
    #t.create(random.sample(range(100), 10))
    print("Inorder:")
    t.inorder()

    res = t.topdown()
    print("topdown: %s" %res)
    
    t.delete(13)
    t.delete(14)
    t.delete(8)
    res = t.topdown()
    print("topdown: %s" %res)
    t.delete(7)
    res = t.topdown()
    print("topdown: %s" %res)
    t.delete(9)
    res = t.topdown()
    print("topdown: %s" %res)
    t.clear()
    print("root: %s" %t.root)
