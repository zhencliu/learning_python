import threading
import time


lock = threading.RLock()
i = 0


def myprint_nolock():
    global i
    print(threading.get_native_id(), i)
    time.sleep(1)
    i += 1
    print(threading.get_native_id(), i)


def myprint():
    global i
    with lock:
        print(threading.get_native_id(), i)
        time.sleep(1)
        i += 1
        print(threading.get_native_id(), i)


def test_rlock():
    t1 = threading.Thread(target=myprint)
    t2 = threading.Thread(target=myprint)
    t3 = threading.Thread(target=myprint)
    t1.start()
    t2.start()
    t3.start()



if __name__ == '__main__':
    test_rlock()
