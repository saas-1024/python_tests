import sys

while True:
    try:
        enter = float(input('Input number: '))
        print(100/enter)

    except ValueError:
        print("Value is not numeric")
    except ZeroDivisionError:
        print("We cant divide by zero!!! Sorry")
    else:
        print('Congratulations, dear user')
    finally:
        print("Finally output")

#  print('all is ok')
#  "finally" working always

    urls = ['text.txt', 'text2.txt', 'text3.txt', 'text4.txt']
    list_defect = []
    list_info = []

    try:
        for url in urls:
            try:
                r = open(url)
                list_info.append(r.read())
                print('okek')
            except FileNotFoundError:
                list_defect.append(url)
                print('not okek')
                continue
    finally:
        rer = open('save.txt', 'a')
        for i in list_info:
            rer.write(i)
        rer.write(str(list_defect))
        rer.close()
        print("all changes saved")

