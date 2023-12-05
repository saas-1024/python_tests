from tkinter import *
import random, time


def brosok():
    x = random.choice(['kost1.png', 'kost2.png', 'kost3.png', 'kost4.png', 'kost5.png', 'kost6.png', ])
    return x


def img(event):
    global b1, b2
    for i in range(25):
        b1 = PhotoImage(file=(brosok()))
        b2 = PhotoImage(file=(brosok()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.18)
    #  root.update()


root = Tk()
root.geometry('400x200')
root.title('Игра в кости. Take an opportunity')
root.resizable(height=False, width=False)  # Window is not resizible
root.iconphoto(True, PhotoImage(file=('icon.png')))
font = PhotoImage(file=('holst.png'))
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)  # Расположение метки на окне программы
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)  # Для будущих вариантов бросков
root.bind('<1>', img)
img('event')
#  Button(root, text='Drop', command=img).pack()
root.mainloop()
