from collections.abc import Iterable


# 遍历字典
def iteration1(d):
    if isinstance(d, Iterable):
        for key in d:
            print(key, d[key])
    return


print('遍历字典:')
d = {'a': 1, 'b': 2, 'c': 3}
iteration1(d)


# 遍历字符串
def iteration2(str):
    if isinstance(str, Iterable):
        for s in str:
            print(s)
    return


print('遍历字符串:')
iteration2("abc123")


# 遍历列表
def iteration3(list):
    if isinstance(list, Iterable):
        for value in list:
            print(value)
    return


print('遍历列表:')
list = [12, 23, 'ad', 'cd']
iteration3(list)


# 遍历元组
def iteration4(tuple):
    if isinstance(tuple, Iterable):
        for value in tuple:
            print(value)
    return


print('遍历元组:')
t = (12, 23, 'ad', 'cd')
iteration4(t)


# 遍历下标
def iteration5(list):
    if isinstance(list, Iterable):
        for i, value in enumerate(list):
            print(i, value)
    return


print('遍历下标:')
t = [12, 23, 'ad', 'cd']
iteration5(t)


# for循环里，同时引用了两个变量，在Python里是很常见的
def iteration6(list):
    if isinstance(list, Iterable):
        for i, y in list:
            print(i, '--', y)
    return


list2 = [(1, 1), (2, 4), (3, 9)]
print('引用了两个变量:')
iteration6(list2)
