#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    ds.TreeNode

    An implementation for tree node.
'''
class TreeNode:
    def __init__(self, value = None):
        self._value = value
        self._left  = None
        self._right = None
        self._parent= None
        self._ref   = 1
        self._height= 0

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def ref(self):
        return self._ref

    @ref.setter
    def ref(self, value):
        self._ref = value
    
    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
    
    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
