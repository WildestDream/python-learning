# -*- coding: utf-8 -*-
try:
    f = open("data")  # 获读取当前目录下的 data 文件
    print(f.name)
    print(f.mode)
    res = f.read()
    print("read:", res)
finally:
    if f:
        f.close()
# add
# 更加优雅的写法, 不需要显示的关流
with open(file='data', mode='r', encoding='utf-8', errors='ignore') as f:
    print(f.read())

# 每次读取一行,遇到编码错误直接忽略ignore
print("每次读取一行:")
with open(file='data', mode='r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())  # # 把末尾的'\n'删掉

# 读取二级制文件
f = open('hadern.png', 'rb')
image_bytes = f.read()
print(len(image_bytes) / 1000, "kB")

# 写文件
with open('msg', 'w', encoding='utf-8') as f:
    f.write("I'm learning python IO")

# 小练习：拷贝照片
with open('copy_image.png', 'wb') as copy_file:
    copy_file.write(image_bytes)
