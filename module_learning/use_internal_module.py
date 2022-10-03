#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module_learning """

__author__ = 'xf'

# 引入 module: sys
import sys


def test():
    # 第一个参数是文件名
    args = sys.argv
    print(args)


# 只有在命令行下执行，该if才满足
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
if __name__ == '__main__':
    test()

# 特殊变量 __XX__
print(__author__)  # xf
print(__doc__)  # a test module_learning
print(__name__)  # __main__
