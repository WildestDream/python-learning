# -*- coding: utf-8 -*-


# 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。
# _name : private, 可以访问，不建议
# __name：private, 不可以直接访问，需要提供 set 方法
# __name__：特殊变量，可以直接访问

# __field 代表私有变量，无法访问
# _field 代表私有变量，可以访问，但是不建议，而且调用方法的时候 pyCharm 也不会提示该方法
class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self._job = 'sales'

    def print(self):
        print(self.__name, self.__age)

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age


s = Student('xf', 29)
s.print()
s.setName('cc')
s.setAge(28)
s.print()
print(s._job)  # _name 可以访问，但是不建议
print(s._Student__name)  # __name 不能直接访问，但是可以访问 _Student__name，但是也不建议这么做

"""
请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
"""


class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise TypeError('Gender is illegal')

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise TypeError('name is illegal')

    def get_gender(self):
        return self.__gender


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
