import uuid


class _UpdateCommand(object):
    action = None


class _AllocateCommand(_UpdateCommand):
    action = 'allocate'
    def __call__(*args):
        print(*args)


class ResMgr(object):
    """
    A resource manager is used to manage cluster resources.
    This class is only used for resoure management APIs, not open to others.
    """

    def __init__(self, config=None):
        self._allocated = dict()  # {resource uuid: resource object}
        self._update_handlers = dict()
        for cls in _UpdateCommand.__subclasses__():
            self._update_handlers[cls.action] = cls

    def myprint(self):
        pass

    def meet(self, request):
        pass

    def do_action(self):
        action = 'allocate'
        obj = self._update_handlers[action]()
        obj(1, 'lzc')
