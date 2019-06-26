'''
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
'''


def generator1():
    print('generator1-----------')
    g = (x * x for x in range(10))
    for x in g:
        print(x)
    return


generator1()


def fib(max):
    print('fib-----------')
    n, a, b = 0, 0, 1
    while (n < max):
        a, b = b, a + b
        n += 1
        print(a, '--', b)
    return 'done'


fib(5)

p = [1]


def generator2():
    p = [1]
    print('generator2----------------')
    i = 0
    while True:
        print(p)
        p = [1] + [p[x] + p[x + 1] for x in range(len(p) - 1)] + [1]
        # print(p)
        i += 1
        if i == 10:
            break


generator2()
