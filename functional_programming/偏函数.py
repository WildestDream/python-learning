# -*- coding: utf-8 -*-

# 通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点

res = int('101011010100', base=2)
print(res == 2772)


# 也可以专门定制一个函数，用于转换二进制数
def int2(arg):
    return int(arg, base=2)


print(int2('101011010100') == 2772)

# 通过 functools 定义一个偏函数 int2 ，也可以解决上述问题
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
import functools

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
# 这里，固化的是 dict 参数，相当于
# int2('1001') 相当于
# int('1001', {'base':2})
int2 = functools.partial(int, base=2)
print(int2('101011010100') == 2772)

# 新定义的偏函数也可以调整 base 的值
print(int2('101011010100', base=10) == 101011010100)

# 偏函数也可以固化 *args
max10 = functools.partial(max, 10)
print(max10(1, 3, 4, 5) == 10)  # 相当于 max(10,1,3,4,5)
