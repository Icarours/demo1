# def enroll(name, gender):
#     print("name:", name)
#     print("gender:", gender)


def enroll(name, gender, age=6, city="BeiJing"):
    print("name:", name)
    print("gender:", gender)
    print("age:", age)
    print("city:", city)


enroll("Jack", "M")
enroll("张三", "M", 23, "HuBei")
enroll('Bob', 'M', 7)
# 默认参数虽然编译运行都没有问题,但是变量会出现红色警告
enroll('Adam', 'M', 17, 'Tianjin')



