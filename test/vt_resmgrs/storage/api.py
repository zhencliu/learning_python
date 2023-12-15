from ..resmgr import ResMgr


class StorageResMgr(ResMgr):

    def meet(self, request_params):
        return True if 'storage_type' in request_params else False

    def myprint(self):
        print('I am in StorageResMgr')


storage_resmgr = StorageResMgr()


__all__ = ['storage_resmgr']
