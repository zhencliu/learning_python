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
     
    def _delete(self, node, parent):
        if node.left is None and node.right is None:
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
        else:
            sub_tree, n, p = None, None, None

            if node.left is not None:
                n = self._max(node.left)
                sub_tree = node.left
            elif node.right is not None:
                n = self._min(node.right)
                sub_tree = node.right

            node.value = n.value
            node.ref = n.ref
            n, p = self._find(sub_tree, n.value)
            self._delete(n, p)
    
    def _min(self, tree):
        node = tree

        if node is None:
            return None
        else:
            while node.left is not None:
                node = node.left
            return node

    def _max(self, tree):
        node = tree
        
        if node is None:
            return None
        else:
            while node.right is not None:
                node = node.right
            return node

    def _find(self, tree, value):
        n, p = tree, None 

        while n is not None:
            if n.value == value:
                break
            else:
                p = n

                if value < n.value:
                    n = n.left
                else:
                    n = n.right
        
        return n, p

    def find(self, value):
        return self._find(self.root, value)
                    
    def delete_recur(self, value):
        node, parent = self.find(value)
        
        if node is not None:
            if node.ref > 1:
                node.ref -= 1
            else:
                self._delete(node, parent)
           
            self._count -= 1

    def delete(self, value):
        node, parent = self._find(self.root, value)

        if node is not None:
            self.count -= 1

            if self.count == 0:
                # An empty tree
                self.root = None
            else: 
                node.ref -= 1

                # Remove the node from tree if reference is 0
                if node.ref == 0:
                    if node.left is None and node.right is None:
                        # 1. node is the leave
                        if value < parent.value:
                            parent.left = None
                        else:
                            parent.right = None
                    elif node.left is not None:
                        # 2. node has left child, node<-max(node.left)
                        #    remove max(node.left)
                        maxnode, parent = self._find(node.left, 
                                                     self._max(node.left).value)
                        node.value, node.ref = maxnode.value, maxnode.ref

                        if parent is None:
                            # 2.1 node.left has NO right sub tree, it's the max one
                            #       node
                            #       /
                            #     maxnode
                            #      /
                            #    subtree
                            node.left = maxnode.left
                        else:
                            # 2.2 node.left has right sub tree
                            #       node
                            #       /
                            #     node.left
                            #      /   \
                            # subtree  parent
                            #            \
                            #           maxnode
                            #            /
                            #          subtree
                            parent.right = maxnode.left
                    elif node.right is not None:
                        # 3. node has right child, node<-min(node.right)
                        #    remove min(node.right)
                        minnode, parent = self._find(node.right, 
                                                     self._min(node.right).value)
                        node.value, node.ref = minnode.value, minnode.ref

                        if parent is None:
                            # 3.1 node.right has NO left sub tree, it's the min one
                            #   node
                            #     \  
                            #    minnode
                            #       \
                            #      subtree
                            node.right = minnode.right
                        else:
                            # 3.2 node.right has left sub tree
                            #       node
                            #         \ 
                            #       node.right
                            #        /   \
                            #    parent  subtree
                            #     / 
                            #  minnode
                            #    \ 
                            #    subtree
                            parent.left = minnode.right

    def insert_recur(self, value):
        new = TreeNode(value)
        new.ref = 1

        if self.empty():
            self._root = new
        else:
            self._insert(self._root, new)
        
        self._count += 1
    
    def insert(self, value):
        node, parent = self._find(self.root, value)

        if node is not None:
            # 1. The data exists, reference++
            node.ref += 1
        else:
            new = TreeNode(value)
            new.ref = 1
            
            # 2. The data doesn't exist
            if parent is None:
                # 2.1 An empty tree, this is the root node
                self.root = new
            else:
                # 2.2 Insert the node as parent's left or right child
                if value < parent.value:
                    parent.left = new
                else:
                    parent.right = new
        
        self._count += 1

    def create(self, iterator):
        for val in iterator:
            self.insert(val)

    def min(self):
        n = self._min(self.root)
        return None if n is None else n.value

    def max(self):
        n = self._max(self.root)
        return None if n is None else n.value

if __name__ == '__main__':
    import random

    t = BSTree();
    l = random.sample(range(100), 6) * 2
    t.create(l)
    print("Inorder:")
    t.inorder()
    print("Preorder:")
    t.preorder()
    print("Postorder:")
    t.postorder()

    print("min: %s" %t.min())
    print("max: %s" %t.max())
    
    res = t.topdown()
    print("topdown: %s" %res)
    print("bottomup: %s" %res[::-1])

    print("Del root: %s" %t.root.value)
    t.delete(t.root.value)
    print("Inorder:")
    t.inorder()
    t.delete(t.root.value)
    print("Inorder:")
    t.inorder()

    t = BSTree()
    l = random.sample(range(100000), 10000)
    t.create(l*2)
    assert t.find(l[1000])[0].value == l[1000]

    for i in l:
        t.delete(i)

    print(t.count)
    print(t.root)
    
    for i in l:
        t.delete(i)

    print(t.count)
    print(t.root)
