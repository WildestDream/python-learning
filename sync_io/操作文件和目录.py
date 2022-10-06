# -*- coding: utf-8 -*-
import os

# 如果是posix，说明系统是Linux、Unix或Mac OS X，
# 如果是nt，就是Windows系统。
print(os.name == 'posix')

# 要获取详细的系统信息，可以调用uname()函数, 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
# posix.uname_result(sysname='Darwin', nodename='feixiaodeMacBook-Pro.local',
# release='21.3.0', version='Darwin Kernel Version 21.3.0: Wed Jan  5 21:37:58 PST 2022; root:xnu-8019.80.24~20/RELEASE_ARM64_T6000',
# machine='x86_64')
print(os.uname())

# 环境变量
envs = os.environ.items()
for k, v in envs:
    print(k, ':', v)

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下

print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
os.path.join('/Users/fox', 'test-dir')

if not os.path.exists('/Users/fox/test-dir'):
    # 创建目录
    os.mkdir('/Users/fox/test-dir')
if os.path.exists('/Users/fox/test-dir'):
    # 删除目录
    os.rmdir('/Users/fox/test-dir')

# 文件名的拆分
print(os.path.split("/path/to/file.txt"))  # ('/path/to', 'file.txt')
print(os.path.splitext('/path/to/file.txt'))  # ('/path/to/file', '.txt')

# 文件的重命名、删除
# os.rename('test.txt', 'test.py')
# os.remove('test.py')


# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
#
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充

# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码
# 注意： listdir 会列出文件以及目录（包含文件！！！）
l = [x for x in os.listdir('/Users/fox/module') if os.path.isdir(os.path.join('/Users/fox/module', x))]
print(l)

# 要列出所有的.py文件，也只需一行代码
pys = [x for x in os.listdir('/Users/fox/module') if os.path.isfile(os.path.join('/Users/fox/module', x))
       and os.path.splitext(x)[1] == '.py']
print(pys)


# 练习
# 利用os模块编写一个能实现dir -l输出的程序。

def dir_l(path):
    print("========= dir -l =========")
    dirs = os.listdir(path)
    for d in dirs:
        if os.path.isdir(os.path.join(path, d)):
            print(d)


dir_l('/Users/fox')


# # 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def find_dirs(key, path):
    print(os.path.abspath(path))
    for d in os.listdir(path):
        fullpath_dir = os.path.join(path, d)
        if os.path.isfile(fullpath_dir) and key in os.path.split(fullpath_dir)[1]:
            print("match:", fullpath_dir[27:])
        elif os.path.isdir(fullpath_dir):
            find_dirs(key, fullpath_dir)


find_dirs('test', '/Users/fox/PycharmProjects')
