#!/usr/bin/env python3

import six
from functools import reduce

def f(a, b=None, **ks):
    print(a)
    print(b)
    print(ks)


def ff(image='image1'):
    def _ff():
        print(image)
    _ff()
    image = 'image2'
    _ff()


def fff(a):
    if a == 1:
        pass
    else:
        print(a)
    return a


def _convert_blkdev_args1(args):
    new_args = {}
    aux = {}
    for key, value in six.iteritems(args):
        if value in ('on', 'yes'):
            value = True
        elif value in ('off', 'no'):
            value = False

        d = new_args
        parts = key.split(".")
        for i, part in enumerate(parts[:-1]):
            if part.isdigit():
                continue

            tmpkey = '.'.join(parts[:i+2])
            if part not in d:
                if parts[i+1].isdigit():
                    # e.g. server.0.host, {'server': [{'host': xx}]}
                    d[part] = [{}]
                    aux[tmpkey] = d[part][-1]
                    d = d[part][-1]
                else:
                    # e.g. server.host, {'server': {'host': xx}}
                    d[part] = {}
                    d = d[part]
            else:
                if parts[i+1].isdigit():
                    if tmpkey in aux:
                        # e.g. server.0.type,
                        # {'server': [{'host': xx, 'type': xx}]}
                        d = aux[tmpkey]
                    else:
                        # e.g. server.1.host,
                        # {'server': [{'host': xx, xx}, {'host':xx}]}
                        d[part].append({})
                        aux[tmpkey] = d[part][-1]
                        d = d[part][-1]
                else:
                    d = d[part]
        d[parts[-1]] = value

    return new_args


def _convert_blkdev_args(args):
    new_args = {}
    aux = {}
    for key, value in six.iteritems(args):
        if value in ('on', 'yes'):
            value = True
        elif value in ('off', 'no'):
            value = False

        d = new_args
        parts = key.split(".")
        for i, part in enumerate(parts[:-1]):
            if part.isdigit():
                # the index, e.g. 0 in server.0.xxx
                continue

            tmpkey = '.'.join(parts[:i+2])
            if part not in d:
                if parts[i+1].isdigit():
                    # e.g. server.0.host, {'server': [{'host': xx}]}
                    d[part] = [dict()]
                    aux[tmpkey] = d[part][-1]
                    d = d[part][-1]
                else:
                    # e.g. server.host, {'server': {'host': xx}}
                    d[part] = dict()
                    d = d[part]
            else:
                if parts[i+1].isdigit():
                    if tmpkey in aux:
                        # e.g. server.0.type,
                        # {'server': [{'host': xx, 'type': xx}]}
                        d = aux[tmpkey]
                    else:
                        # e.g. server.1.host,
                        # {'server': [{'host': xx, xx}, {'host':xx}]}
                        d[part].append(dict())
                        aux[tmpkey] = d[part][-1]
                        d = d[part][-1]
                else:
                    d = d[part]
        d[parts[-1]] = value

    return new_args

import six
def flatten_dictionary1(d):
    result = {}
    stack = [iter(six.iteritems(d))]
    keys = []
    while stack:
        for k, v in stack[-1]:
            keys.append(k)
            if isinstance(v, dict):
                stack.append(iter(six.iteritems(v)))
                break
            else:
                result['.'.join(keys)] = v
                keys.pop()
        else:
            if keys:
                keys.pop()
            stack.pop()
    return result


def _flatten_dict(source, target, prefix=None):
    for k, v in six.iteritems(source):
        key = "%s" % k if not prefix else '%s.%s' % (prefix, k)
        if isinstance(v, dict):
            _flatten_dict(v, target, key)
        else:
            t[key] = v

def convert(args):
    new_args = {}
    tmp = {}
    for key, val in six.iteritems(args):
        if val in ('on', 'yes'):
            val = True
        elif val in ('off', 'no'):
            val = False
        if '.' in key:
            sub_key = key.split('.')
            reduce(lambda d, k: d.setdefault(
                k, {}), sub_key[1:-1], tmp)[sub_key[-1]] = val
            new_args[sub_key[0]] = tmp
        else:
            new_args[key] = val
    return new_args

from collections import OrderedDict

def convert2(args):
    new_args = dict()
    for key, value in six.iteritems(args):
        parts = key.split(".")
        d = new_args
        for part in parts[:-1]:
            if part not in d:
                d[part] = dict()
            d = d[part]
        d[parts[-1]] = value
    return new_args


if __name__ == '__main__':
    t = {}
    prefix = 'server.0'
    d0 = {}
    d1 = {'x': 1}
    d2 = {'aaa': 'on', 'node-name':'rbd_node','driver':'raw','file.driver':'gluster','file.server.0.host':'10.66.8.135','file.server.0.type':'inet','file.server.0.port':'12345', 'file.volume':'gv0','file.path':'lzc.raw', 'file.server.1.path':'/tmp/socket','file.server.1.type':'unix', 'file.server.2.host':'10.66.8.136','file.server.2.type':'inet', 'file.server.2.port':'11111'}
    d3 = {'aaa': 'off', 'node-name':'iscsi_node','driver':'iscsi','transport':'tcp','portal':'10.66.10.26:3260','target':'iqn.2019-09.com.example:zhencliu', 'lun':'0', 'user':'redhat', 'password-secret':'sec1'}
    d4 = {'node-name':'nbd_image1','driver':'nbd','server.type':'inet','server.host':'dhcp-8-135.nay.redhat.com','server.port':'10809','cache.direct':'on','cache.no-flush':'off'}
    #print(d4)
    #print(convert2(OrderedDict(d4)))
    #print(d0)
    #print(convert2(OrderedDict(d0)))
    print('before')
    print(d4)
    print('after')
    print(convert(OrderedDict(d4)))
