from .cvm import cvm_resmgr
from .storage import storage_resmgr
from .network import network_resmgr


class _Dispatcher(object):

    def __init__(self):
        self._resmgrs = list()

    def dispatch(self, request_params):
        for mgr in self._resmgrs:
            if mgr.meet(request_params):
                return mgr
        return None

    def register(self, mgr):
        self._resmgrs.append(mgr)


_resmgr_dispatcher = _Dispatcher()
_resmgr_dispatcher.register(cvm_resmgr)
_resmgr_dispatcher.register(storage_resmgr)
_resmgr_dispatcher.register(network_resmgr)


#__all__ = ['_resmgr_dispatcher']
