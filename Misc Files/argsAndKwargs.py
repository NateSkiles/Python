def myFun(*args):
    for arg in args:
        print(arg)


myFun('This is an example of args', 'string', 'and then an integer', 5)


def myFun2(**kwargs):
    print("kwargs", kwargs)


myFun2(first="1", second="2", third="3")
