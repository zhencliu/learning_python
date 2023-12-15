#!/usr/bin/python3
import re

def fun():
    urls = [
        'gluster://1.2.3.4/testvol/a.img',
        'gluster+tcp://1.2.3.4:24007/testvol/dir/a.img',
        'gluster+tcp://[1:2:3:4:5:6:7:8]/testvol/dir/a.img',
        'gluster+tcp://[1:2:3:4:5:6:7:8]:24007/testvol/dir/a.img',
        'gluster+tcp://server.domain.com:24007/testvol/dir/a.img',
        'gluster+unix:///testvol/dir/a.img?socket=/tmp/glusterd.socket',
        'gluster+rdma://1.2.3.4:24007/testvol/dir/a.img'
    ]

    p = re.compile(r'gluster\+?(?P<type>.+)?://((?P<host>[^/]+?)(:(?P<port>\d+))?)?/(?P<volume>.+?)/(?P<path>[^,?]+)(\?socket=(?P<socket>[^,]+))?')

    for url in urls:
        m = p.match(url)
        print('---------------------------------')
        print(url)
        print(m.group('type'))
        print(m.group('host'))
        print(m.group('port'))
        print(m.group('volume'))
        print(m.group('path'))
        print(m.group('socket'))
        print('---------------------------------')


if __name__ == "__main__":
    fun()
