import os

lists_paths = []

for adres, papka, file in os.walk('C:\\'):
    for i in file:
        full_path = os.path.join(adres, i)
        lists_paths.append(full_path)

r = open('text.txt', 'w')
for x in lists_paths:
    r.write(x + '\n')

r.close()

