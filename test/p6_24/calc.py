def calc(num):
    sum = 0
    for n in num:
        sum = sum + n * n
    return sum


'''
num可以是可变参数,可以传入列表,也可以传入元组
'''

x = calc([1, 2, 3, 4])
print(x)

x = calc((1, 2, 3, 4, 7))
print(x)


def calc2(*num):
    sum = 0
    for n in num:
        sum = sum + n * n
    return sum


'''
形参为*num,可以直接传入多个数字.或者传入列表(元组)的变量名*nums,在变量名nums前面加一个*

*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
'''

print(calc2(1, 2, 3))
nums = [1, 2, 3]
print(calc2(*nums))

nums2 = (1, 2, 3)
print(calc2(*nums2))
print(calc2(nums2[0], nums2[2]))
