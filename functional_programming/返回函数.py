# -*- coding: utf-8 -*-

def lazy_sum(args):
    # 定义一个函数 sum
    def sum():
        temp = 0
        for i in args:
            temp += i
        return temp

    # 返回函数 sum
    return sum

# 返回的 sum 就是一个闭包，因为它持有了上下文的引用
# java 中没有闭包的概念，但是通过匿名函数，以及λ表达式模拟了闭包
# java 中持有的外部的引用必须是 final 的，只读，更加的安全
# python 中的闭包，持有外部引用，不仅可读，而且可以修改(配合 nonlocal 关键字)
# 闭包延长了上下文对象的生命周期


args = [1, 2, 3]
sum1 = lazy_sum(args)
print(sum1() == 6)

sum2 = lazy_sum(args)
print(sum2() == 6)

print(sum1 == sum2)  # False，lazy_sum 每次都会返回新的函数

args.append(4)
print(args)
print(sum1())  # 10
print(sum2())  # 10


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())  # 9
print(f2())  # 9
print(f3())  # 9


# nonlocal
def inc():
    x = 0

    def fn():
        # x += 1,  # 对外部变量 x 不能修改，只能读取
        return x ** 2

    return fn


# 若想修改外部的变量，必须使用 nonlocal 关键字
def inc():
    x = 0

    def fn():
        nonlocal x
        x += 1
        return x ** 2

    return fn

fn = inc()
print(fn() == 1)
print(fn() == 4)
print(fn() == 9)
print(fn() == 16)


# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    i = 0

    def counter():
        nonlocal i
        i += 1
        return i

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
