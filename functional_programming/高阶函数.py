# -*- coding: utf-8 -*-

# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)


res = add(1, -2, abs)
print(res == 3)


def cal(x):
    return x ** 2


def cal2(x, y, calu):
    return calu(x) + calu(y)


print(cal2(1, 2, cal) == 5)
