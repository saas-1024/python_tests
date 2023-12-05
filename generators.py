import os
h = [9,8,7,6,5,4,3,2,1,5,5,-2]

newh = []
for x in h:
    newh.append(x*2)
print(newh)

newh2 = [x for x in h]  # Примерно в 2 раза быстрее append
print(newh2)

z = {x*x for x in h}  # hash-table
print(z)

f = {x: x*2 for x in h}  # dict
print(f)

#  If in generator

print(' with if ')
#  g = [x for x in h if x % 2 == 0]
g = [x for x in h if x % 2 == 0 and x > 0]
print(g)
print(type(g))

#  dict generator based on another dict
# g = [os.path.join(z, i) for z, x, c in os.walk('C:\\') for i in c if '.txt' in i]
# print(len(g))

price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}
new_price = {}
for i in price.keys():
    new_price[i] = round(price[i] * 0.85, 2)

new_d = {i: round(price[i]*0.85, 2) for i in price.keys()}
print(new_d)

#  Generator in () brackets instead of [] in iterator
