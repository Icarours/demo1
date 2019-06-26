#!/usr/bin/python3
import math

a = input("请输入a")
b = input("请输入b")
c = input("请输入c")

print("输入a,b,c的值---", a, b, c)


def fun(a, b, c):
    m = b * b - 4 * a * c
    if m >= 0:
        x1 = (-b + math.sqrt(m)) / (2 * a)
        x2 = (-b - math.sqrt(m)) / (2 * a)
        return x1, x2
    else:
        print("b*b - 4*a*c<0")
        return 0


r = fun(int(a), int(b), int(c))

print("result=", r)

# 求解一元二次方程
'''
原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

小结
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。

'''




