# -*- coding: utf-8 -*-


# dist 迭代
d = {'a': 1, 'b': 2, 'c': 3}

for k in d:
    print(k)

for k in d.values():
    print(k)

for k in d.items():
    print(k)

for k, v in d.items():
    print(k, v)

# str 迭代
s = "abc"
for c in s:
    print(c)

# list 迭代，携带 index
L = ['A','B','C','D','E']
for index, value in enumerate(L):
    print(index, value)
