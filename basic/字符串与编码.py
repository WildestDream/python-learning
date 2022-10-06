# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python 3的字符串使用Unicode，直接支持多语言

# 一个unicode字符表示为:01001110|00101101
# 也可以表示为一个整数（0-65535），也可以进一步表示成两个16进制数（两个字节）

# 表示方式1，一个整数
c = "中"
# 字符 "中" 转换为 unicode 整数
print("ord", ord(c))  # 20013
print("chr", chr(20013))  # 中

# 表示方式2，两个 16进制数，每个两位的16进制数代表一个字节
# 01001110 == 4e
# 00101101 == 2d
# 字符 "中" 转换为 unicode 的两个字节(两个16进制数: 4e, 2d)，\u 代表 unicode 字符
print('\u4e2d')  # 中

#  utf-8 , gbk

# bytes类型的数据用带b前缀的单引号或双引号表示
# 但是这里的编码方式是 ascii，因此 b'中文' 会报错
x = b'ABC'

print("bytes", len(x), x)  # bytes 3 b'ABC'

# 支持中文的编码方式
x = '中文'.encode('utf-8')
print("utf-8 bytes", len(x), x)  # bytes 6 b'\xe4\xb8\xad\xe6\x96\x87' 每个中文字符在 utf-8 下3个字节, \x 表示后面的数是 16进制

x = '中文'.encode('gbk')
print("gbk bytes", len(x), x)  # bytes 4 b'\xd6\xd0\xce\xc4' 每个中文字符在 gbk 下2个字节，\x 表示后面的数是 16进制

# 解码
x = b'ABC'.decode('ascii')
print("原文", x)

x = b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8")  # 编解码的方式必须一致
print("原文", x)

x = b'\xe4\xb8\xad\xef'.decode("utf-8", errors='ignore')  # 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print("原文", x)

# 格式化,
# %d 整数, %f浮点数, %s字符串, %x十六进制整数
str = "hello, my name is %s" % 'xf'
print(str)

# 若想表示 %, 需要使用 %% 转义
str = "hello, your score is 80.12%% %s" % 'at all'
print(str)

user = "name:%s, gender:%s, age:%d" % ('xf', 'M', 29)
print(user)

# 字符串的 format
str = 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('xf', 1.1755)
print(str)

# f-string
r = 2.5
s = 3.14 * r ** 2
format_str = f"The area of a circle with radius {r} is {s:.3f}"
print(format_str)