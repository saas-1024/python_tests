h = [
    'https:\\www.site.com',
    'https:\\www.leftsite.com',
    'https:\\www.rightsite.com',
    'https:\\www.capitalistsite.com',
    'https:\\www.cykabilyatsite.com'
]
import os

n = [x.split('\\') for x in h if '.com' in x]  # generator of list
print(n)
print(type(n))

z = (x.split('\\')[1] for x in h if '.com' in x)  # generator expression
for i in z:
    print(i)

print(type(z))
#  next function in generator
print(help(next))

n = [x for x in os.walk('D:\\')]
print('here we n')
z = (y for y in os.walk('D:\\'))
print('here we z')

print(len(n))
print(n.__sizeof__())
print(z.__sizeof__())
next(z)
