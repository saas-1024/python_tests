import os

s = "Lets write a string as 's'"
s2 = 'Let\'s write a string as "s"'
print(s)
print(s2)

#  with \ we can move string to the next line and divide string
s3 = "Lets write a stri\nng as 's'"
print(s3)

url = 'https:\www.youtube.com\\new'
url2 = r'https:\www.youtube.com\new'
print(url2)
os.walk('D:\\')
print("kek\n\n\n\n\n")

#  methods for working with str type

str = 'stroka texta'
print(str[3:11])
print('sto' in str)

print(str.upper())
print(str.capitalize())
print(str)
path = 'C:/Users/PYHS/Desktop/s.py'
path1 = path.replace('/', '\\')
print(path1)

rer = path1.split('\\')
print(rer)
print(rer[-1])

q = open('formatstr.txt')
print(q.read())
rer1 = q.read()
list_znaki = ['(', ')', '"', '"']
for i in list_znaki:
    rer1 = rer1.replace(i, '')
print(rer1)

rer2 = rer1.split()
print(rer2)

enter = input("Your name: ")
s = 'Hello %s, I am %s' % (enter, 'Python')
print(s)

s1 = 'Hello {1}, I am {0}'.format(enter, 'Python')
print(s1)

s3 = f'Hello {enter}, I can do it in f-string {2+2}'
print(s3)


