from .top import Top
from .sub.sub import Sub


def f():
    for cls in Top.__subclasses__():
        obj = cls()
