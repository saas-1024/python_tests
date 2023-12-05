# r = open('file.txt')
# r.write('something' + '\n')
# 10/0
# r.write('cho cho')
# r.close()
#
# print('All is ok')

with open('file.txt', 'a') as r:
    r.write('ssdsdsd' + '\n')
    # 10/0
    r.write('dfsadsa')

print("all is ok")


