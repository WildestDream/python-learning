# -*- coding: utf-8 -*-
from collections.abc import Iterable,Iterator


print(isinstance([], Iterable))  # True
print(isinstance("abc", Iterable))  # True
print(isinstance(100, Iterable))  # False
print(isinstance((1, 2), Iterable))  # True


# list、dict、str等数据类型不是Iterator，但是是 Iterable
print(isinstance([], Iterator))  # False
print(isinstance("abc", Iterator))  # False
print(isinstance(100, Iterator))  # False
print(isinstance((1, 2), Iterator))  # False

"""
Iterator:惰性计算， 只能 next, 不能 for
Iterable:一次性存储内存，可以 for，但是 for 的本质还是调用 Iterator
"""

for x in [1, 2, 3, 4, 5]:
    pass

# 通过迭代器遍历 list
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break