# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 切片，含头不含尾
print(L[0:3])

print(L[:3])

print(L[:-1])

print(L[:-2])

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(L[:10:2])  # [1, 3, 5, 7, 9]

# 复制
L2 = L[:]
L2.append(11)
print("L", L)
print("L2", L2)

# tuple 也可以切片，切片下来的还是一个 Tuple
t = (0, 1, 2, 3, 4, 5)[:3]
print(t)

# 字符串也可以切片
str = 'ABCDEFG'[1:3]
print(str)  # BC
