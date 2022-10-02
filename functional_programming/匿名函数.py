# -*- coding: utf-8 -*-

f = lambda x: x ** 2

print(f)  # <function <lambda> at 0x108954430>

print(f(2) == 4)

# 请用匿名函数改造下面的代码：

"""
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
"""

L = list(filter(lambda x: x % 2 == 0, range(1, 20)))

print("odd list", L)
