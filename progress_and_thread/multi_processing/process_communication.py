# -*- coding: utf-8 -*-
import os
from multiprocessing import Queue, Process
from time import sleep

# process 通信两种方式：
# 方式1：通过 Queue,
# 方式2：通过 Pipes （见：subprocess_test.py）
def read_task(q):
    while True:
        item = q.get(True) #True => block get
        print("queue is ", hash(q))
        print('process %s read data %s' % (os.getpid(), item))
        sleep(0.5)


def write_task(q):
    for i in range(10):
        q.put(i)
        print('process %d write %d' % (os.getpid(), i))
        sleep(1)
    pass


if __name__ == '__main__':
    # 注意：只有使用 multiprocessing 中的 Queue，才可以在不同的 Process 中共享
    # 这里若把 q 换成 list，read task 读取到的集合一直是空的，因为 list 的更新在写进程，读进程无法感知
    q = Queue()
    w_process = Process(target=write_task, args=(q,))
    r_process = Process(target=read_task, args=(q,))
    w_process.start()
    r_process.start()
    w_process.join()
    r_process.terminate()
    print("finished...")