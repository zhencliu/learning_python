from .dispatcher import _resmgr_dispatcher


def create_resource(request_params):
    """
    Create a resource by the request, note only a logic cluster resource is
    created, without any real resource allocation on any worker node.

    :param request_params: The params describing the resource requirement,
                           converted from user's cartesian params
    :type request: Params
    :return: The resource uuid
    :rtype: string
    """

    mgr = _resmgr_dispatcher.dispatch(request_params)
    #mgr.myprint()
    mgr.do_action()
