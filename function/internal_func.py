# -*- coding: utf-8 -*-
import math

print(max(1, 2, 3, 10))

print(min(1, 2, 3, 10))

# 数据类型转换
int('123')

int(12.34)

float('12.34')

str(1.23)

bool(1)  # True

bool('')  # False

print(hex(65))

# 获取绝对值
abs(-10)

# 函数引用
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个"别名"
f = abs
print(f(-12))


# 自定义函数, 求和
def my_sum(n):
    l = list(range(0, n + 1))
    res = 0
    for item in l:
        res += item
    return res


print("求和函数:", my_sum(100))


# 在其他函数中调用，需要：from 包名.文件名 import 函数名

# 自定义函数，求绝对值

def my_abs(x):
    # isinstance() 函数来判断一个对象是否是一个已知的类型
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 自定义函数，打印
def my_print(msg):
    print(msg)


# pass 占位符，没想好写啥的时候，否则代码编译不过
def nop():
    pass


# 返回值为多个
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


r = move(100, 100, 60, math.pi / 6)
print(r)  # (151.96152422706632, 70.0) 返回实际是一个 tuple

x, y = move(100, 100, 60, math.pi / 6)  # 也可以这样接收一个 tuple
print(x, y)
