# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print1_10(xer):
    while xer < 11:
        print(xer)
        xer += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

i = 0
print1_10(i)

# factorial
x = 1
count = 0
number = int(input())
while count < number:
    count += 1
    x *= count
else:
    print(x)

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьъэюя'
str_ = input("Input str:\n")
for i in alphabet:
    count = 0
    for r in str_:
        if i == r:
            count += 1
    if count > 0:
        print("Букв ", i, " было ", count)

for x in range(1, 10, 2):
    print(x)

# python lists
m = [1, 2, 1, 3, 5]
print(m[0])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
