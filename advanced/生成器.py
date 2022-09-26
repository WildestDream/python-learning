# -*- coding: utf-8 -*-

"""
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator

创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator

generator 有状态
"""

generator = (x for x in range(1, 5))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator))  # 没有元素了，抛出异常：StopIteration


generator = (x for x in range(1, 11))
for x in generator:
    print(x)


# yield 理解
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


o = odd()
print(next(o))  # step 1, 1
print(next(o))  # step 2, 3
print(next(o))  # step 3, 5

# 练习，杨辉三角形
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

i = 0
l0 = [1]

i = 1
l1 = [1, 1]

i = 2
l2 = [1, l1[0] + l1[1], 1]

i = 3
l3 = [1, l2[0] + l2[1], l2[1] + l2[2], 1]

i = 4
l4 = [1, l3[0] + l3[1], l3[1] + l3[2], l3[2] + l3[3], 1]

print(l0)
print(l1)
print(l2)
print(l3)
print(l4)


# def triangles():
#     L = [1]
#     while True:
#         yield L[:]
#         L.insert(0, 0)
#         for a in range(0, len(L) - 1):
#             L[a] = L[a] + L[a + 1]
#
# g = triangles()
# for x in g:
#     print(next(g))