# -*- coding: utf-8 -*-
import types

# type

print(type(123))  # <class 'int'>
print(type('str'))  # <class 'str'>


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


class Animal(object):
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


# 但是 type 不能跟父类比较，否则返回 false
print(type(Dog()) == Dog)  # True
print(type(Dog()) == Animal)  # False

# 跟父类也可以对比，使用 isinstance
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
print(isinstance(Dog(), Dog) == True)
print(isinstance(Dog(), Animal) == True)

# dir 函数

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
infos = dir('abc')
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
# '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
# 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
# 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
# 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace',
# 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
# 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
print(infos)

# hasattr，setattr，getattr
d = Dog()
# 判断对象是否含有某属性/方法
print(hasattr(d, 'age'))
# 设置对象的某属性/方法
setattr(d, 'age', 8)
# 获取对象的某个属性、方法
print(getattr(d, 'age'))
# 获取对象的某个属性、方法（没有该属性的话，返回默认值）
print(getattr(d, 'name', '旺财'))


# 一个正确的用法的例子如下：
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取
def readData(fp):
    pass


def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
