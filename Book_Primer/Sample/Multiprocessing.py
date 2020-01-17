'''
Sample of multiprocessing
'''

import multiprocessing
import os


def do_this(what):
    whoami(what)


def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))


if __name__ == "__main__":
    whoami("main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this, args=("function %s" % n,))
        p.start()

