# -*- coding: utf-8 -*-

l = [1, 2, 3, 4, None, 5, 6, 0]

# 求偶数序列，filter 返回的仍然是惰性序列
r = filter(lambda x: x and x % 2 == 0, l)

print(list(r))


# 得到素数序列

# 得到初始化序列 generator 3,5,7,9,11,13,...
def gen_l():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def gen_prime_number():
    yield 2
    it = gen_l()
    while True:
        num = next(it)
        yield num
        # it = filter(lambda x: x % num > 0, it)  # 这样写是错误的，这样写其实传入的时钟是一个lamda
        it = filter(_not_divisible(num), it)  # 要保证每次传入的lamda是新的，而不是修改之前的


g = gen_prime_number()
for pn in g:
    if pn <= 100:
        print("素数:", pn)
    else:  # 没有这一句程序会不停的运行
        break


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
# def is_palindrome(n):
#     if n is None:
#         return True
#     s = str(n)
#     if len(s) == 1:
#         return True
#     start = 0
#     end = len(s) - 1
#     while start <= end:
#         if s[start] != s[end]:
#             return False
#         start += 1
#         end -= 1
#     return True

# 方法2，占用2倍的内存
def is_palindrome(n):
    n = list(str(n))
    return n == n[::-1]


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
