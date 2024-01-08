from ..resmgr import ResMgr


class NetworkResMgr(ResMgr):

    def meet(self, request_params):
        return True if 'nettype' in request_params else False

    def myprint(self):
        print('I am in NetworkResMgr')


network_resmgr = NetworkResMgr()


__all__ = ['network_resmgr']
