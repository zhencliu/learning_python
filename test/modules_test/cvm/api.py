from ..resmgr import ResMgr


class CVMResMgr(ResMgr):

    def myprint(self):
        print('I am in CVMResMgr')

    def meet(self, request_params):
        return True if 'vm_secure_guest_type' in request_params else False


cvm_resmgr = CVMResMgr()


__all__ = ['cvm_resmgr']
