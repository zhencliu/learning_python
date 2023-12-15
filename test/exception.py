import ipaddress


def _is_ipv6_addr(addr):
    try:
        ipaddress.IPv6Address(addr)
    except ipaddress.AddressValueError:
        pass
        print('after pass')
        return False
    return True


def _test1():
    try:
        1/0
    except:
        pass


def _test2():
    1/0


if __name__ == '__main__':
    print(_is_ipv6_addr('abcd'))
    _test1()
    _test2()
