def multiply(i):
    return i * i;


y = lambda x: x * x

print(y(3))
print(multiply(3))


# my lambda
def myfunc(n):
    return lambda a: a * n


mytripler = myfunc(3)
z = int(input())
print(mytripler(z))
