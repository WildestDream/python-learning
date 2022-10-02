# -*- coding: utf-8 -*-
import functools
import time


def now():
    print("2022-10-02")


# 获取函数的名称
funcName = now.__name__

print(funcName == 'now')

"""
现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator"""


# log 就是一个装饰器，可以对函数 func 进行增强
def log(func):
    def wrapper(*args, **kw):
        # 在调用函数 func 前，打印日志：func 的函数名
        print("invoke", func.__name__)
        return func(*args, **kw)  # 这样传参可以让改函数支持传入任何的参数

    return wrapper


# @log 相当于 log = log(show_list)
@log
def show_list(args):
    print(args)


"""
打印：
invoke show_list
[1, 3, 5]
"""
show_list([1, 3, 5])


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


"""
The list are: show_list
[2, 4, 6]
"""


# now = log('execute')(show_list)
@log('The list are:')
def show_list(args):
    print(args)


show_list([2, 4, 6])

show_list = log('execute')(show_list)
print(show_list.__name__ == 'show_list')  # 通过注解 @functools.wraps，将以前的函数名 func 复制给当前的函数 wrapper

"""
练习
请设计一个 decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools
def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn
"""


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start_time = time.perf_counter()
        res = func(*args, **kw)
        print(f'func {func.__name__} cost time:{time.perf_counter() - start_time:.8f} s')
        return res

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# 练习： 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

def log_around(func):
    def wrapper(*args, **kwargs):
        print('begin call')
        res = func(*args, **kwargs)
        print('end call')
        return res

    return wrapper


@log_around
def test():
    print("test")


test()

"""
练习 再思考一下能否写出一个@log的decorator，使它既支持：
@log
def f():
    pass
    
又支持：

@log
def f():
    pass
"""


def log(input='xf'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg, **kwargs):
            print('invoke', input)
            res = func(*arg, **kwargs)
            return res

        return wrapper

    return decorator


@log()
def f():
    pass


f()


@log('cc')
def f():
    pass


f()
