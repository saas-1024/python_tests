from dis import *


def some(x):
    return x/5


var = lambda x: x/5  # lambda is anonymous function as people call it
print(var(8934))

print(some(22324))
print(dis(some))
print(dis(var))

print(some(7))  # division by zero examples
print(var(543))

list_of = [['Adam', 22], ['Hui', 322], ['Chlen', 27], ['Obama', 44], ['Cyka', 3222], ['Backs', 242]]


def s(x):
    return x[1]


r = sorted(list_of, key=s)
print(r)
print('  Next example as lambda func  ')
r = sorted(list_of, key=lambda x: x[1])
print(r)

z = filter(lambda x: x[1] > 18, list_of)
print(z)
