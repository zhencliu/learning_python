#!/usr/bin/env python3

class A(object):
    def __init__(self):
        super().__init__()
        self.a = 'a'
        print("A:init")

    def func1(self):
        print("A: func1")


class B(object):
    def __init__(self):
        super().__init__()
        self.b = 'b'
        print("B:init")

    def func1(self):
        print("B: func1")


class C(B, A):
    def __init__(self):
        print("C:init")
        super().__init__()

    def func1(self):
        super(C, self).func1()

if __name__ == '__main__':
    obj = C()
    print(C.__mro__)
    #obj.func1()
    #print(obj.b)
    #print(obj.a)
