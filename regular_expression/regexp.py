# -*- coding: utf-8 -*-

import re

# match success, return Match obj
# use r'', - 可以不用转义，否则需要写成 /-
m = re.match(r'^\d{3}-\d{3,8}$', '010-12345')
print(m is not None)

# match failed, return None
m = re.match(r'^\d{3}-\d{3,8}$', '010-12345w')
print(m is None)

# 切分字符串
arr = re.split(r'\s+', 'a b   c')
print(arr == ['a', 'b', 'c'])  # 识别多个连续的空格

arr = re.split(r'[\s,]+', 'a,b, c  d')
print(arr == ['a', 'b', 'c', 'd'])

arr = re.split(r'[\s,;$]+', 'a,b;; $ c  d')
print(arr == ['a', 'b', 'c', 'd'])

# 分组
res = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(res[0] == '010-12345')  # 第0个元素永远是原字符串
print(res[1] == '010')
print(res[2] == '12345')
print(res)

res = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345').groups()
print(res == ('010', '12345'))

# 贪婪匹配
# 最后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
# 举例如下，匹配出数字后面的0

print(re.match(r'^(\d+)(0*)$', '102300').groups() == ('102300', ''))

# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。

# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：

print(re.match(r'^(\d+?)(0*)$', '102300').groups() == ('1023', '00'))

# 编译
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
# 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 用编译后的正则表达式去匹配字符串。
# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
res = re_telephone.match('010-12345').groups()
print(res == ('010', '12345'))

"""
练习
请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

someone@gmail.com
bill.gates@microsoft.com
"""


def is_valid_email(addr):
    return re.match(r'^[\w.]+@\w+.com$', addr) is not None


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

"""
版本二可以提取出带名字的Email地址：

<Tom Paris> tom@voyager.org => Tom Paris
bob@example.com => bob
"""


def name_of_email(addr):
    # 注意: ()? 中的 () 并不是分组的含义，但是() 内部假如有 ()，那就是分组了
    match_res = re.match(r'^(<(\w+\s*\w+)>)?\s*(\w+)@\w+.\w+$', addr)
    if match_res:
        print(match_res.groups())
        if match_res.groups()[1]:
            return match_res.groups()[1]
        else:
            return match_res.groups()[2]
    raise TypeError('Not match!')


# 测试:
print("=========")
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
