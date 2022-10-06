# -*- coding: utf-8 -*-
from io import StringIO, BytesIO

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口


# StringIO
# 内存缓冲区，读写 String
# 可以 seek
try:
    s = StringIO()

    s.write('hello')
    s.write(' ')
    s.write('world!')

    res = s.getvalue()
    print(res == 'hello world!')

    # 需要 reset 标志位
    s.seek(0)
    while True:
        line = s.readline()
        if line == '':
            break
        print(line.strip())
finally:
    if s:
        s.close()

# 在StringIO中构建字符串，直接读取
try:
    s = StringIO('hello\nworld\nmy friends')
    while True:
        line = s.readline()
        if line == '':
            break
        print(line.strip())
finally:
    if s:
        s.close()

# BytesIO
try:
    b = BytesIO()
    b.write('我爱你'.encode('utf-8'))
    res = b.getvalue()
    print(len(res) == 9)
    print(res == b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0')

    b.seek(0)
    res = b.read()
    print(res == b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0')
finally:
    if b:
        b.close()
