# -*- coding: utf-8 -*-

class Student(object):
    pass


# todo 打印的内存地址一样，是单例？
print(Student())
print(Student())
print(Student())


class Teacher(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printMsg(self):
        print("name is %s, age is %d" % (self.name, self.age))


# todo 打印的内存地址和 Student 一样？
print(Teacher('xf', 29))
print(Teacher('cc', 28))

t = Teacher('xf', 29)
t.printMsg()

# python 可以动态地为实例添加新的属性 salary
t1 = Teacher('t1', 35)
t1.salary = 10000
t1.printMsg()
print("salary is %s" % t1.salary)

# 实例 t2 没有添加新的属性 salary, 因此访问报错
t2 = Teacher('t2', 31)
t2.printMsg()

# print("salary is %s" % t2.salary)  # AttributeError: 'Teacher' object has no attribute 'salary'
