#!/usr/bin/python3

def fun(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


print(fun(2))
print(fun(2, 3))
