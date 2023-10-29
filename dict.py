d1 = {'a': 7, 'b': 22}
d2 = dict([[1,2], [3,4]])
d3 = dict.fromkeys('1')

price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}

users = {
    'Alex777': {'password': 123, 'id': 112}
    }


def buy():
    pay = 0
    while True:
        enter = input('Что покупаем?\n')
        if enter == 'end':
            break
        pay += price[enter]
    return pay


print(users['Alex777']['password'])

d5 = d1.copy()
print(d1.items())
print(d1.keys())
print(d1.values())
d1.update(d2)
print(d1)

#  for i in price:
#     price[i] += 0.1

print(price)

new_price = {}
for i in price:
    new_price[i] = round(price[i] + 0.1, 2)

print(new_price)

new_price_dict = {}
for key, value in price.items():
    print(key)
    print(value)

for key, value in price.items():
    new_price_dict[value] = key
print(new_price_dict)

for value in price.values():
    print(value)

for key in price.keys():
    print(key)
