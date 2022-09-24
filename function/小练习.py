# -*- coding: utf-8 -*-

# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解。
import math


def solve2(a, b, c):
    # 校验参数
    if not isinstance(a, (int, float)):
        raise TypeError("a must be a number")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be a number")
    if not isinstance(c, (int, float)):
        raise TypeError("c must be a number")
    # 判断是否有解
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Do not exist solves")
        return None, None
    # 开始计算
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2


x1, x2 = solve2(1, -3, 2)
print(x1, x2)  # 2.0 1.0

x1, x2 = solve2(1, 0, 1)
print(x1, x2)  # None None
