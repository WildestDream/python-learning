# -*- coding: utf-8 -*-
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：


def trim(s):
    if not isinstance(s, str):
        raise TypeError("input must be string type")

    length = len(s)
    if length == 0:
        return ''

    i = 0
    while i < length and s[i] == ' ':
        i += 1

    j = length - 1
    while j >= 0 and s[j] == ' ':
        j -= 1

    if j < i:
        return ''
    return s[i:j + 1]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    if len(L) == 1:
        return L[0], L[0]
    min = L[0]
    max = L[0]
    for v in L:
        if v < min:
            min = v
        if v > max:
            max = v
    return min, max

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
