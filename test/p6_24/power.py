def power(x):
    return x * x


def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


print("2的平方=", power(2))
print("2的3次方=", power(2, 3))
print("2的4次方=", power(2, 4))
print("10的平方=", power(10))
