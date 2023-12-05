# def decor(f):
#     def wrapper():
#         print('Decorator code')
#         f()
#         print('Decorator code 2')
#     return wrapper
#
#
# @decor  # make = decor(make)
# def make():
#     enter = input('Enter something...')
#     print(enter)
#
#
# print('Here -> ')
# make()

def decor(f):
    def wrapper():
        try:
            h = f()
        except Exception:
            print('Repeat number input...')
            h = f()
        return h
    return wrapper


@decor  #  make
def make():
    enter = float(input('Input number: '))
    return enter


@decor
def make2():
    enter = float(input('Input number again: '))
    return enter


make2()
make()
