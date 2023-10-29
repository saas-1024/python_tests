import time

x = (1, 2, 3, 4, 5, 6, 7)
y = [1, 2, 3, 4, 5, 6, 7]
u = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7}
h = {1, 2, 3, 4, 5, 6, 7}

print(x.__sizeof__())
print(y.__sizeof__())
print(u.__sizeof__())
print(h.__sizeof__())

z = list(range(10000))
r = list(range(5000, 15000))
p = list(range(10000, 20000))


def f(*args):
    list_new = []
    for i in args:
        for y in i:
            if y not in list_new:
                list_new.append(y)
    return list_new


start = time.time()
f(z, r, p)
stop = time.time() - start
print(stop)

start2 = time.time()
z_set = set(z)
t = z_set.union(set(r), set(p))
stop2 = time.time() - start2
print(stop2)

#  operations with python sets

z = {1, 2, 3, 4, 5}
x = {3, 4, 5, 6, 7}
z.add(6)
z.discard(6)
#  z.update(x)
sec = z.intersection(x)
print(sec)

#  Form the list of words from the text file
new_set = set()
reader = open('text.txt')
reader2 = open('text.txt')
new_set.update((set(reader.read().split())))

print(new_set)
#  Words of unique words from 2 different sets

new_set2 = new_set.intersection(set(reader2))
print("kek\n")
print(new_set2)
reader.close()
reader2.close()
