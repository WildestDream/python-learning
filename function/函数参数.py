# -*- coding: utf-8 -*-
import math


# 默认参数
# 默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个
def my_pow(x, n=2):
    return math.pow(x, n)


print(my_pow(10) == 100)
print(my_pow(10, 3) == 1000)


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# 调用传参的时候，顺序可以变化，但是此时要注明 key
enroll('xf', 'M', city='XIAN')
enroll('xf', 'M', age=29)


# 错误写法
# def add_end(L=[]):
#     L.append('END')
#     return L

# 正确写法，默认参数必须是不可变的
# 否则函数将变为有状态
def add_end(l=None):
    if l is None:
        l = []
    l.append("END")
    return l


# 可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n ** 2
    return sum


print(calc([1, 2, 3]) == 14)


# 在函数内部，参数numbers接收到的是一个tuple
# 因此 numbers 是不可变的，无法修改，更加的安全
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n ** 2
    return sum


print(calc(1, 2, 3) == 14)

# 如果已经有了一个 list，例如
list = [1, 2, 3]
# 可以直接传入 *list，而不必：calc(nums[0], nums[1], nums[2])
print(calc(*list) == 14)


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    kw.clear()


person('xf', 29)
person('xf', 29, city='xian')
person('xf', 29, city='xian', dept='IT')

# **kw 是对外部的参数 dict 的拷贝，修改 kw 的值，不会对外部的参数 dict 造成影响
dict = {'city': 'xian', 'dept': 'IT'}
person('xf', 29, )
print("dict", dict)  # 不变


# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


# 命名关键字参数限制传入的 key 必须符合要求
person('xf', 29, city='xian', job='it')
# person('xf', 29, city='xian')  # TypeError: person() missing 1 required keyword-only argument: 'job'
# person('xf', 29, city='xian', job='it', sports='ball')  # TypeError: person() got an unexpected keyword argument 'sports'


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('xf',29,1,2,3,city='xian',job='java dev')
