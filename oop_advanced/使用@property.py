# -*- coding: utf-8 -*-


# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


# 赋值、获取值通过方法，略显繁琐
s = Student()
s.set_score(90)
print(s.get_score())


class Student(object):

    def __init__(self):
        self._name = 'China Boy'

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # name 属性没有 @name.setter 注解，因此只读
    @property
    def name(self):
        return self._name


# 通过注解@property，@score.setter，赋值、获取值通过属性，更加的易懂，同时又可以在真正的方法增加参数校验逻辑
d = Student()
d.score = 90
print(d.score)
print(d.name)
# d.name = 'xf'  # AttributeError: can't set attribute, 只读

# 注意：属性名与方法名不能相同，否则会报：RecursionError: maximum recursion depth exceeded

"""
请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
"""


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, v):
        self._width = v

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, v):
        self._height = v

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
