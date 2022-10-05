# -*- coding: utf-8 -*-
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


# Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
print(type(Hello))  # <class 'type'>
print(type(Hello()))  # <class '__main__.Hello'>


# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义

# 先定义函数
def fn(self, name='world'):
    print('Hello, %s.' % name)


# 通过 type 方法创建类型 Hello
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class
Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
h.hello('China')
h.hello()

print(type(Hello))  # <class 'type'>
print(type(h))  # <class '__main__.Hello'>


# metaclass
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

# metaclass是类的模板，所以必须从`type`类型派生：

# 举例，给自己的 MyList 添加一个 add 方法
class ListMetaclass(type):
    # __new__()方法接收到的参数依次是：
    # 当前准备创建的类的对象；
    # 类的名字；
    # 类继承的父类集合；
    # 类的方法集合。
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


my_list = MyList()
my_list.add('a')
my_list.add('b')
my_list.add('c')
print(my_list)

# 而一般的 list 并没有 add 方法


# meta class 使用案例 ORM 框架
"""
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
"""

print("============ ORM ============")


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        # attrs.items() 打印所有的属性如下：
        # __module__ -> __main__
        # __qualname__ -> User
        # id -> <IntegerField:id>
        # name -> <StringField:username>
        # email -> <StringField:email>
        for k, v in attrs.items():
            print(k, "->", v)
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        # 修改类的属性，将一部分的映射关系放到 __mappings__ 里，然后删除冗余属性
        # 修改类的属性，将表明放到 __table__里
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        # __mappings__, __table__ 来自于父类ModelMetaclass的动态生成
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


# 这里的 Model 类似 spring jpa 里的 UserRepository，这里的 xxxField 类似需要与表字段映射的注解
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
    salary = 100  # 不会插入，因为不是 field 类型


u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()


# 可以再定义一个新的类型，很方便, 此时这个框架的优势就体现出来了
class Student(Model):
    id = IntegerField("id")
    grade = StringField("grade")
    age = IntegerField("grade")


s = Student(id='0504001', name='xf', grade='chu 3')
s.save()
