# -*- coding: utf-8 -*-

# 引入module: module_learning.m1
import module_learning.m1

# import numpy

# 调用其它 module 的方法
module_learning.m1.testfunc()

# private 函数，可以调用，但是有警告
res = module_learning.m1._cal2(2)
print(res == 4)