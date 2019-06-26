# 生成list列表
list1 = list(range(1, 11))
print('list1:', list1)


def list2():
    li = []
    for x in range(0, 10, 2):
        li.append(x * x)
    print('list2--', li)
    return


list2()


def list3():
    li = []
    for x in range(0, 10):
        li.append(x * x)
    print('list3--', li)
    return


list3()


def list4():
    var = [x * x for x in range(1, 11)]
    print('list4--', var)


list4()


# 使用两层循环，可以生成全排列
def list5():
    x = [m + n for m in 'ABC' for n in 'XYZ']
    print('list5--', x)
    return


list5()


def list6():
    x = [x * x for x in range(1, 11) if x % 2 == 0]
    print('list6--', x)
    return


list6()


def list7():
    r = [x * x for x in range(1, 11) if x * x % 2 == 1]
    print('list7--', r)
    return


list7()

import os


# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
def list8():
    r = [d for d in os.listdir('.')]
    print('list8--', r)
    return


list8()


# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
def dic1():
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    for k, v in d.items():
        print(k, '---', v)
    return


dic1()


def list9():
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    r = [k + '--' + v for k, v in d.items()]
    print('list9--', r)
    return


list9()


# 将列表中的大些字母全部转化为小写字母
def list10():
    x = ['Hello', 'World', 'IBM', 'Apple']
    r = [s.lower() for s in x]
    print("list10--", r)
    return


list10()


def list11():
    x = ['Hello', 'World', 14, 'IBM', 'Apple']
    r = [s.lower() for s in x if isinstance(s, str)]
    print("list11--", r)
    return


list11()


# 先判断列表中的元素是否字符串,如果是,就将字符串转化为小写,加入列表;如果不是字符串,就直接加入新的列表
def list12():
    x = ['Hello', 'World', 14, 'IBM', 'Apple']
    r = []
    for s in x:
        if isinstance(s, str):
            r.append(s.lower())
        else:
            r.append(s)
    print("list12--", r)
    return


list12()

'''
写列表生成式时，把要生成的元素的表达式放到前面，后面跟for循环，就可以把list创建出来，
'''
