# -*- coding: UTF-8 -*-

# Filename : 03-function-scopy.py
# author by : （学员ID)

# 目的:
# 掌握变量作用域

total = 0 # 这是一个全局变量

# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total

#调用sum函数
# total = sum( 10, 20 )
sum( 10, 20 )
print ("函数外是全局变量 : ", total)
