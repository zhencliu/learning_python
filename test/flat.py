#!/usr/bin/env python3


import six


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
    d = 'file: json:{"driver": "luks", "file": {"pool": "rbd", "image": "rhel810-64-virtio-scsi.luks", "driver": "rbd"}, "key-secret": "image1_encrypt0"}'
    for (k, v) in traverse_nested_dict(d):
        print(k, v)
