# -*- coding: utf-8 -*-
import os
from multiprocessing import Process
from time import sleep


def run(arg):
    sleep(3)
    print("process %d running %s" % (os.getpid(), arg))


if __name__ == '__main__':
    print('process %s start' % os.getpid())
    # 可传入参数：
    # def __init__(self, group=None, target=None, name=None, args=(), kwargs={},*, daemon=None):
    p = Process(target=run, args=('child',))
    p.start()
    p.join()
    print('process %s finished' % os.getpid())
