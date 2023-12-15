#!/usr/bin/env python3


import six
from multiprocessing import Pool

def traverse_nested_dict(d):
    iters = [six.iteritems(d)]
    while iters:
        item = iters.pop()
        try:
            k, v = next(item)
        except StopIteration:
            continue
        iters.append(item)
        if isinstance(v, dict):
            iters.append(six.iteritems(v))
        else:
            yield k, v


if __name__ == '__main__':
    def f(x):
        return x*x
    ff = lambda x: x*x
    with Pool(4) as p:
        p.map(ff, [1, 2])
