# -*- coding: utf-8 -*-

"""
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
"""

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
# print(d['xf'])  # key 不存在报错，KeyError: 'xf'
print(d.get('xf'))  # 通过 get 方法，不存在返回 None
print(d.get('xf', 100))  # 不存在返回默认值 100

# 删除 k-v
d.pop("Bob")
print(d)

# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = {1, 2, 2, 3}
print(s)  # {1, 2, 3}

s.add(4)
print(s)

s.remove(4)
print(s)

s1 = {1, 2, 3}
s2 = {1, 2, 4}
# 交集
print(s1 & s2)
# 并集
print(s1 | s2)
