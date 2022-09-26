# -*- coding: utf-8 -*-
l = [x * x for x in range(1, 11)]
print(l)

l = [x * x for x in range(1, 11) if x % 2 == 0]
print(l)

# 双层循环
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C'}

dt = [k + "->" + v for k, v in d.items()]
print(dt)

# 小练习, 获取小写元素列表（跳过数字以及None）
L = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L if isinstance(x, str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
