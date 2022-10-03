# -*- coding: utf-8 -*-

class Student(object):
    name = 'tw'  # 类属性


print(Student.name == 'tw')

s = Student()
print(s.name == 'tw')  # 通过实例也可以访问类属性

s.name = 'thoughtworks.com'  # 实例属性覆盖类属性
print(s.name)

s.__delattr__('name')  # 删除实例属性，类属性重新生效
print(s.name)

"""
为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
"""


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
