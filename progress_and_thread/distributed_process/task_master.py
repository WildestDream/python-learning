import queue
from multiprocessing.managers import BaseManager

"""
                                             │
┌─────────────────────────────────────────┐     ┌──────────────────────────────────────┐
│task_master.py                           │  │  │task_worker.py                        │
│                                         │     │                                      │
│  task = manager.get_task_queue()        │  │  │  task = manager.get_task_queue()     │
│  result = manager.get_result_queue()    │     │  result = manager.get_result_queue() │
│              │                          │  │  │              │                       │
│              │                          │     │              │                       │
│              ▼                          │  │  │              │                       │
│  ┌─────────────────────────────────┐    │     │              │                       │
│  │QueueManager                     │    │  │  │              │                       │
│  │ ┌────────────┐ ┌──────────────┐ │    │     │              │                       │
│  │ │ task_queue │ │ result_queue │ │<───┼──┼──┼──────────────┘                       │
│  │ └────────────┘ └──────────────┘ │    │     │                                      │
│  └─────────────────────────────────┘    │  │  │                                      │
└─────────────────────────────────────────┘     └──────────────────────────────────────┘
                                             │

                                          Network
"""
class QueueManager(BaseManager):
    pass


task_queue = queue.Queue()


def return_task_queue():
    return task_queue


result_queue = queue.Queue()


def return_result_queue():
    return result_queue


QueueManager.register('get_task_queue', callable=return_task_queue)
QueueManager.register('get_result_queue', callable=return_result_queue)

if __name__ == '__main__':
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(100):
        print('向队列中插入了数字%d' % i)
        task.put(i)

    print('尝试从结果队列中取出结果')
    try:
        for i in range(100):
            r = result.get(timeout=100)
            print("结果：%s" % r)
    except queue.Empty:
        print('结果队列为空')

    manager.shutdown()
    print("主服务关闭")
