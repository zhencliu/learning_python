#!/usr/bin/env python3

import re

def outer(arg):
    def inner():
        print(arg)
    inner()


def is_ok(p, s):
    return re.search(p, s, re.M) is not None

def args(**p):
    print(p)
    del p['romfile']
    print(p)


if __name__ == '__main__':
    p = 'lzca|abc'
    s = '''
    abab
    lzac
    lzc
    xxxxx
    '''
    if is_ok(p, s):
        print('true')
    else:
        print('false')

    d = {'a':1, 'romfile':'romfile'}
    args(**d)
    print(d)
