#!/usr/bin/env python3


def f(a, b=None, **ks):
    print(a)
    print(ks)
    initiator = access.iscsi_initiator if (access
                                           and access.storage_type == 'iscsi-direct') else None


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


if __name__ == '__main__':
    servers = [dict(zip(['host', 'type', 'port'],
                        [host, image_access.transport, image_access.port])) for host in image_access.peers]
    if servers:
        socket = "?socket=%s" % params.get(
            "gluster_unix_socket") if vol_uri.startswith(
            "gluster+unix:") else ""
    export_name = params.get('nbd_export_name') if params.get(
        'nbd_export_name') else ''

    print(b)
    s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa  bb'
