# -*- coding: utf-8 -*-
from enum import Enum, unique

# 定义方式1，定义 Month 类型的枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# Jan -> 1
# Feb -> 2
# Mar -> 3
# Apr -> 4
# May -> 5
# Jun -> 6
# Jul -> 7
# Aug -> 8
# Sep -> 9
# Oct -> 10
# Nov -> 11
# Dec -> 12
for item in Month:
    print(item.name, "->", item.value)


## 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
@unique
class Month(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 访问枚举的方式

print(Month.Mon)
print(Month.Thu)

print(Month(0))
print(Month(1))
print(Month(6))

"""
把Student的gender属性改造为枚举类型，可以避免使用字符串：
from enum import Enum, unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
"""


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        if not isinstance(gender, Enum):
            raise TypeError("gender must be enum")
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
