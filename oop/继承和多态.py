# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print("Animal is running...")


class Tiger(Animal):
    pass


class Dog(Animal):
    pass


t = Tiger()
t.run()

d = Dog()
d.run()

print(isinstance(t, Animal) == True)
print(isinstance(d, Animal) == True)


class Bird(Animal):
    def run(self):
        print("Bird is flying...")

b = Bird()
b.run()

# 多态
# 编写一个函数，这个函数接受一个Animal类型的变量：
def run(animal):
    animal.run()

run(Bird())
run(Tiger())
run(Dog())

# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证传入的对象有一个run()方法就可以了
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
class Person(object):
    def run(self):
        print("person is running...")

run(Person())
