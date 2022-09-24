#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 整数

# 可以处理任意大小的整数，且允许 _ 分割
a = 10000_0000_0000_0000_0000

# 浮点数
b = 1.23e9  # 代表:1.23x10的9次方

c = 1.2e-5

print(b, c)

# 字符串
str1 = "abc"

str2 = 'abc'

# \ 转义
str3 = "I\'m xiaofei"

print(str1, str2, str3)

# r'' 表示''中的 \ 不会转义
print('\\\t\\')  # \	\
print(r'\\\t\\')  # \\\t\\

str4 = "hello\n"
print(str4)

# 文本块
str5 = """
{
    "bucket": "bucket-test",
    "key": "k1",
    "file": "test"
}
"""
print(str5)
print("str len", len(str5))

str6 = '''
{
    "bucket": "bucket-test",
    "key": "k1",
    "file": "test"
}
'''

print(str6)

# r 也可以用于文本块
str7 = r'''
{
    "bucket": "bucket-test \n",
    "key": "k1 \n",
    "file": "test \n"
}
'''

print(str7)

# 布尔值
print(True)
print(False)
print(3 > 2)

age = 18
if age >= 18:
    print("man")
else:
    print("child")

# None
print(None)

# 赋值, 同一个变量可以反复赋值，而且可以是不同类型的变量
# 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错
# 和静态语言相比，动态语言更灵活，就是这个原因

# Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。
# 对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向。
num = 1
print(num)
num = "hello"
print(num)

a = 'ABC'
b = a
a = 'XYZ'
print("b =", b)  # ABC

# 常量
# 在Python中，通常用全部大写的变量名表示常量
# 但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法
PI = 3.14159265359
print(PI)

# 除法
num = 10 / 3
print("num", num)  # num 3.3333333333333335

num = 10 / 2
print("num", num)  # num 5.0, 即使可以整除，结果仍为浮点数

# 地板除 //，结果为整数，向下取整
num = 10 // 3
print("num", num)  # num 3
