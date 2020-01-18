'''
Sample of Thread
'''

import threading

def do_this(what):
    whoami(what)

def whoami(what):
    print('Thread %s says: %s' % (threading.current_thread(), what))

if __name__ == "__main__":
    whoami("main program")
    for n in range(4):
        p = threading.Thread(target=do_this, args=("function %s" % n,))
        p.start()

