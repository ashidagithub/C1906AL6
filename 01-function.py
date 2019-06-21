# -*- coding: UTF-8 -*-

# Filename : 01-function.py
# author by : （学员ID)

# 目的:
# 掌握函数的用法

# 练习一：第一个函数
def hello():
    print("Function-Hello World!")
    return

# 调用
hello()

# 练习二：打印指定字符串 - 传入字符串
def printme( str ):
   # 打印任何传入的字符串
   print (str)
   return

# 调用
printme("xxxxx")

# 练习三：计算面积函数 - 传入数字
def area(width, height):
    return width * height

# 调用
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


# 练习四：返回值
