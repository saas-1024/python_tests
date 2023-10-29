print('До функции')


def show():
    print('функция')


def show2():
    x = 7
    return x


def count_list(param):  # we use lists in this function
    count = 0
    for i in param:
        count += 1
    return count


show()
print('После функции')

y = show2()
print(y)

print(" Using function parameters")
#  Using functions and their parameters

j = [9, 8, 7, 6]
h = ['a', 'b', 'h']
k = [9, 8, 7, 5, 5, 3]
print(count_list(j))  # argument

print(count_list(h))
print(count_list(k))
print("kek\n\n\n")


#  functions with many arguments
def name(h, *args, key):
    print(h)
    print(args)


name(1, 2 ,3, 5, 5, 6, key=7)


def exclusive_item(*args, key=False):
    new_list = []
    for i in args:
        for y in i:
            if y not in new_list:
                new_list.append(y)
    if key:
        new_list.sort()
    return new_list


z = [9, 8, 7]
x = [8, 8, 9, 7, 6, 5]
c = [1, 2, 3, 4, 5, 6, 7, 7]

t = exclusive_item(z, x, c, key=True)  # named argument for key func parameter
print(t)

