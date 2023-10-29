import os
#  for i in os.walk("D:\\LEARNING_PYTHON"):
#    print(i)

spisok = []

for adres, dirs, files in os.walk("D:\\LEARNING_PYTHON"):
    spisok.append(adres)
print(spisok)
print("kek\n")

for adres, dirs, files in os.walk("D:\\LEARNING_PYTHON"):
    for file in files:
        full = os.path.join(adres, file)
        if '.txt' in full:
            spisok.append(os.path.join(adres, file))
print(spisok)


