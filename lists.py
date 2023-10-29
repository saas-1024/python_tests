m = [[5, 6], [1, 2], ['s', 'f']]
print(len(m))

# list in python can be modified as datatype
m[0] = 9
print(m)

m[1], m[2] = m[2], m[1]
print(m)

m = m + [7]
print(m)

n = list('stroka')
print(n)

new_n = list(range(10))
print(new_n)

k = []
for i in new_n:
    if i == 8:
        continue
    k += [i]
else:
    print(k)

# list methods and cuts
x = [9, 8, 7, 6, 5]
x.append(4)
x.insert(1, 7)
print(x)

x.sort()
print(x)
# pop delete by index, remove delete by value
# clear - clean the full list

# python tuples - unmodified datatype
x = (9, 8, 7, 6)  # x = 9, 8, 7, 6 - same
print(type(x))

x = tuple("stroka")
print(x)

x = (9, 8, 7, 6, 5, 4, 3)  # tuple
# z, c, b = x
# print(z, c, b)
y = []  # list
r = 5
u = 7
r, u = (u, r)  # swap
print(x[1:5])  # срез кортежа тоже кортеж, не список!

for i in range(len(x)):
    y.append(x[i] + 3)

print(y)
t = list(x)
t[0] = 10
x = tuple(t)
print(x)


