# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 python 集合的几个特点
 - 根据下表获取元素，像数组
 - 使用方式，也有栈的特性，append + pop 操作队尾元素
 - 使用方式，也像一个双端队列
 - 元素类型可以不同，没有泛型的说法
"""
# list是一种有序的集合，可以随时添加和删除其中的元素
list = [1, 2, 3]
print(list)

# 返回最后一个元素
print(list[-1])

# 追加
list.append(4)
print(list)

# 插入
list.insert(0, 0)
print(list)
list.insert(1, 1.5)
print(list)

# 删除队尾元素
del_item = list.pop()
print(del_item)
print(list)

# 删除队首元素
del_item = list.pop(0)
print(del_item)
print(list)

# list里面的元素的数据类型也可以不同，比如：
l = ["hello", 1, 1.25, True]
print(l)

# list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
print(len(s))
s = []
print(len(s))

# 元祖 tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
t = (1, 2)
print(t)
print(len(t))
# 获取 tuple 的分量
print("tuple is", t[0], t[1])

# 注意，即使定义一个元素的 tuple，必须加上, 避免被当成括号处理
t = (1,)
print(t, len(t))

# 注意，这是一个空的 tuple
t = ()

# 注意：引用不可变，但是引用的对象可以修改！
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'A1'
t[2][1] = 'B1'
print(t)  # ('a', 'b', ['A1', 'B1'])
