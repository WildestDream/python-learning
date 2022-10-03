# -*- coding: utf-8 -*-

# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()
s.name = 'xf'
s.age = 29
print(s.name)
print(s.age)


# 报错, 因为 score 不在白名单，不允许自动扩展 !
# s.score = 98 # AttributeError: 'Student' object has no attribute 'score'


# 但是 __slots__ 的限制对于子类无效
class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 98
print(g.score)
