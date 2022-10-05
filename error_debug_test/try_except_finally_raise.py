# -*- coding: utf-8 -*-
import logging

try:
    a = 2 / 1
    print(a)
except BaseException as e:
    # 使用 python 自带的日志框架，更好的记录异常
    logging.exception(e)
except ValueError as v_error:
    logging.exception(v_error)
    # 也可以直接抛出 raise, 也可以封装成为其他的异常类型
    # raise
    # raise Exception("input error")
else:
    print("success")
finally:
    print("clear resources")


# 抛出异常

class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


res = foo('1')
print(res)


"""
练习：
运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
"""

print("=========")
from functools import reduce

def str2num(s):
    return float(s)  # 改为 float 即可

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()