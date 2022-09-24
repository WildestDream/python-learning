# -*- coding: utf-8 -*-

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# range(0, 5) 生成序列： [0, 1, 2, 3, 4]
L = list(range(0, 101))
print(L)

# 求和练习
sum = 0
for item in L:
    sum += item

print("sum=", sum)

# while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break
n = 1
while n < 100:
    if n >= 18:
        break
    n = n + 1

print(n)  # 18

# continue
# 偶数求和
sum = 0
l = list(range(0, 10))
for item in l:
    if item % 2 == 1:
        continue
    sum += item
print("sum =", sum)
