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
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
"""