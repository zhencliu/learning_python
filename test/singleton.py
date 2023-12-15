#!/bin/env python3

class StorageSecret(object):
    __instance = None

    def __new__(cls, pool):
        if not StorageSecret.__instance:
            StorageSecret.__instance = object.__new__(cls)
        return StorageSecret.__instance

    def __init__(self, pool):
        self.pool = pool

def f1():
    obj = StorageSecret('lzc')
    print(id(obj), obj.pool)

def f2():
    obj = StorageSecret('lzc')
    print(id(obj), obj.pool)

if __name__ == '__main__':
    f1()
    f2()
    obj = StorageSecret('lzc')
    print(id(obj), obj.pool)
