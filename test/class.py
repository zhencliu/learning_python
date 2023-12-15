#!/usr/bin/env python3

class A(object):
    CGROUP_PATH = '/sys/fs/cgroup'
    M = '{cg}/machine.slice'.format(cg=CGROUP_PATH)

    def __init__(self, arg=False):
        if arg:
            self.arg = 'True'
        else:
            self.arg = 'False'
        print(self.M)

    @property
    @staticmethod
    def sf():
        return 'lzc'

    def print_arg(self):
        print(self.arg)

    def func(self, arg):
        print(arg)

    @staticmethod
    def method(arg):
        A._method(arg)

    @staticmethod
    def _method(arg=M):
        print(arg)

    def func1(self, arg):
        self.method(arg)
        self.func(arg)

    def func2(self, arg=None):
        print(arg)

    def __del__(self):
        print('un-construct')


class AA(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config):
        print('in AA %s' % config)

class BB(AA):
    def __init__(self, config):
        super().__init__(config)
        print('in BB %s' % config)

if __name__ == '__main__':
    o = BB('bb')
    oo = BB('bbb')
    if o is oo:
        print('same')
    #obj = A()
    #A.method('abcde')
    #var = A.sf
    #print(var)
    #obj.func2()
    #obj.func2('lzc')
