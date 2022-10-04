# -*- coding: utf-8 -*-

# __str__ and __repr__

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "student's name is %s" % self.name

    # 控制台进行调试的时候，直接输入变量，打印的内容由函数 __repr__ 决定
    __repr__ = __str__


print(Student('xf'))


# __iter__ and __getitem_
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

# 定义一个可以迭代的斐波那契数列
class Fiber(object):
    def __init__(self):
        self.first, self.second = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.first, self.second = self.second, self.first + self.second
        return self.first

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):  # n 其实就是循环的次数
            a, b = b, a + b
        return a


f = Fiber()
for num in f:
    if num >= 10000:
        break
    print(num)

print("=============")

print(f[0] == 1)
print(f[1] == 1)
print(f[2] == 2)
print(f[3] == 3)
print(f[4] == 5)


# __getattr__
class Teacher(object):
    def __init__(self, name):
        self.name = name

    # 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段
    def __getattr__(self, attr):
        # 动态返回不存在的属性
        if attr == 'subject':
            return "computer"
        # 动态的返回不存在的函数
        if attr == 'work':
            return lambda students_num: print("teach %d students" % students_num)
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


t = Teacher('cc')
print(t.name)  # cc
print(t.subject)  # computer
t.work(10)  # teach 10 students


# 使用场景：实现动态的调用
class Chain(object):
    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        return Chain("%s/%s" % (self.path, path))

    def __str__(self):
        return self.path


invoke_chain = Chain().status.user.timeline.list
print(str(invoke_chain) == '/status/user/timeline/list')

# __call__
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
class Person(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("person is called, name is %s" % self.name)


p = Person('xf')
p('James Hadern')  # 对象可以当函数一样调用，此时，函数与对象的边界已经模糊了

# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，
# 能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例


print(callable('str'))  # False
print(callable([1,2,3])) # False
print(callable(abs)) # True
