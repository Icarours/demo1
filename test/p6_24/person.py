def person(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)
    return


'''
关键字参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，
利用关键字参数来定义这个函数就能满足注册的需求。

和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
'''
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

'''
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
对kw的改动不会影响到函数外的extra。
'''
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

'''
命名关键字参数
对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。

仍以person()函数为例，我们希望检查是否有city和job参数
'''


def person2(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('person2---', 'name', name, 'age', age, 'other', kw)
    return


person2('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


def person3(name, age, *, city, job):
    print('person3---', name, age, city, job)
    return


person3('Jack', 24, city='Beijing', job='Engineer')

'''
小结
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''
