# -*- coding: utf-8 -*-

# map()函数接收两个参数，一个是函数，一个是Iterable, 返回值是一个 Iterator，需要转换为 Iterable
def f(x):
    return x ** 2


# 得到一个 Iterator，直接遍历不方便
g = map(f, [1, 2, 3])

# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break

# 转成 Iterable，方便用 for 遍历
for x in list(g):
    print("next", x)

# 将所有的整数转换为字符串
r = list(map(str, [1, 2, 3]))
print(r)

# reduce 函数

from functools import reduce


def add(a, b):
    return a + b


res = reduce(add, [1, 2, 3, 4])
print("reduce:", res)

# 使用 lamda 表达式
res = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print("reduce:", res)

# 练习 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
input_data = ['adam', 'LISA', 'barT']

res = list(map(lambda s: s.capitalize(), input_data))
print(res)


# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(l):
    return reduce(lambda x, y: x * y, l)


print(prod([2, 3, 5]) == 30)


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(str):
    return float(str)


print(str2float('123.456') == 123.456)
