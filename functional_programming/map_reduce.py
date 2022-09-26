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
