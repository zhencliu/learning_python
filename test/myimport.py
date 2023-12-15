import os
import logging


def f():
    logging.info('pwd = %s', os.path.dirname(__file__))

class A(object):
    def __init__(self):
        print('I am a A obj')
    def f(self):
        print('A.f()')

a = A()
