#!/usr/bin/env python3

import threading
import time


def do_something():
    time.sleep(2)
    print("do_something")
    return True

t = threading.Thread(target=do_something)
t.daemon = True # without the daemon parameter, the function in parallel will continue even your main program ends
t.start()
#t.join() # with this, the main program will wait until the thread ends
print("end of main program")
