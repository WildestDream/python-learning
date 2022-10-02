# -*- coding: utf-8 -*-
import builtins

res = sorted([1, 3, 2, 5])
print(res)

# 按照 abs 的大小排序
res = sorted([36, 5, -12, 9, -21], key=abs)
print(res)

# 按照字典序排序

res = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(res)

res = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(res)

# 练习
# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


res = sorted(L, key=by_name)
print(res)


# 再按成绩从高到低排序

def by_score(t):
    return -t[1]


res = sorted(L, key=by_score)
print(res)
