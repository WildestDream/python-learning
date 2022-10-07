# -*- coding: utf-8 -*-
import os
import threading
from time import sleep

# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们只需要使用 threading 这个高级模块
def loop(n):
    for i in range(n):
        print('process %s thread %s start..., print %d' % (os.getpid(), threading.currentThread().getName(), i))
        sleep(1)
    pass


print('process %s thread %s start...' % (os.getpid(), threading.currentThread().getName()))
t = threading.Thread(target=loop, name='loop-thread', args=(5,))
t.start()
t.join()
print('process %s thread %s end' % (os.getpid(), threading.currentThread().getName()))
