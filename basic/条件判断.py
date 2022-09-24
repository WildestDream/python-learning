# -*- coding: utf-8 -*-
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = [1, 2, 3]
if x:
    print('True')

x = "hello"
if x:
    print('True')

x = 1.5
if x:
    print('True')

x = 0
if x:
    print('True')
else:
    print('False')  # False

"""
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
"""

height = 1.88
weight = 74.8
bmi_value = weight / (height * height)
print("bmi_value:", bmi_value)

if bmi_value < 18.5:
    print("过轻")
elif 18.5 <= bmi_value < 25:
    print("正常")
elif 25 <= bmi_value < 28:
    print("过重")
elif 28 <= bmi_value < 32:
    print("肥胖")
else:
    print("严重肥胖")
