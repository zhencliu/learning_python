#!/usr/bin/env python3

import threading
import time


def do_something():
    time.sleep(2)
    print("do_something")
    return True

def run():
    l = [1, 2]
    def f1(l):
        l = ['a']

    def f2():
        global l
        l = ['b']
        print(l)

    def f3():
        print(l)

    f1(l)
    f2()
    f3()

if __name__ == '__main__':
    run()
