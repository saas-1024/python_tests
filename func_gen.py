# def some():
#     list_text = []
#     with open('file.txt', encoding='utf-8') as r:
#         for x in r:
#             list_text.append(x)
#     return list_text

def some():
    with open('file.txt', encoding='utf-8') as r:
        for x in r:
            yield x


for i in some():
    print(i.split())

p = some()
print('pause coding')
print(p)  # generator for file splitting by rows as coded above

print(next(p))
print(next(p))
print('with cycle next')

for i in p:
    print(i)
