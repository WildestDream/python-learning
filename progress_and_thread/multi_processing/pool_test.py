# -*- coding: utf-8 -*-
import os
from multiprocessing.pool import Pool
from time import sleep


def run_task(i):
    print("task %s start running on process %s..." % (i, os.getpid()))
    sleep(5)
    print("task %s finished  on process %s..." % (i, os.getpid()))


if __name__ == '__main__':
    # default process capacity is cpu cores
    pool = Pool(4)
    # submit 5 tasks but the process pool size is only 4
    for i in range(5):
        pool.apply_async(func=run_task, args=(i,))
    # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
    # 调用close()之后就不能继续添加新的Process了
    pool.close()
    pool.join()
    print("main process %s finished." % os.getpid())