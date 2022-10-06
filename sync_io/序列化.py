# -*- coding: utf-8 -*-
import pickle

# pickle 泡菜

d = dict(name='Bob', age=20, score=88)

# dumps + loads
# 序列化对象为一个 bytes
bs = pickle.dumps(d)

# 从 bytes 反序列化
print("load from bytes", pickle.loads(bs))

# dump + load
# 持久化到磁盘
with open('./dict.obj', 'wb') as f:
    pickle.dump(d, f)

# 从磁盘反序列化
with open('./dict.obj', 'rb') as r:
    d = pickle.load(r)
    print("load from disk", d)  # {'name': 'Bob', 'age': 20, 'score': 88}

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系


# JSON
import json

# dict 序列化 json
j_str = json.dumps(d)
print("serialize to json str", j_str)

d = json.loads(j_str)
print("deserialize from json str", d)

# 持久化 json 串
with open('./dict.json', 'w') as f:
    json.dump(d, f)

# 反序列化 json 串
with open('./dict.json', 'r') as r:
    j_obj = json.load(r)
    print(j_obj)


# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
# class 序列化 json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)


# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


student = Student('xf', 29, 98.0)

print(json.dumps(student, default=student2dict))

# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
j_stu_str = json.dumps(student, default=lambda obj: obj.__dict__)
print(j_stu_str)


# 反序列化
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


obj = json.loads(j_stu_str, object_hook=dict2student)
print(obj)  # <__main__.Student object at 0x108bfc190>

# 练习
# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响

# If ``ensure_ascii`` is false, then the return value can contain non-ASCII
# characters if they appear in strings contained in ``obj``. Otherwise, all
# such characters are escaped in JSON strings.

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)  # {"name": "\u5c0f\u660e", "age": 20}
print(s)
s = json.dumps(obj, ensure_ascii=False)  # {"name": "小明", "age": 20}
print(s)