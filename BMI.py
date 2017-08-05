# -*- coding: utf-8 -*-

from Tkinter import *


def Calculate(a, b):
    x = (float(a) / 100) ** 2
    y = int(b)
    BMI = y / x
    return BMI


def Situation(n):
    if n < 18.5:
        return ("你的體重過輕，多吃一點喔")
    elif 18.5 <= n < 24:
        return ("健康體位，繼續保持^_^")
    elif 24 <= n:
        return ("體位異常，注意飲食!")


def callback():
    a = int(e1.get())
    b = int(e2.get())
    result = Calculate(a, b)
    t.insert("1.0", "你的BMI為:" + format(result, '.2f') + '\n')
    situation = Situation(result)
    t.insert("2.0", str(situation))


master = Tk()
master.title("BMI_Calculator")
Label(master, text="Height (cm)").grid(row=0)
Label(master, text="Weight (kg)").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b = Button(master, text='Calculate', bg='white', command=callback).grid(row=0, column=2)
Button(master, text='Clean', bg='white', command=lambda: t.delete(1.0, END)).grid(row=1, column=2)
Button(master, text='Quit', bg='white', command=master.quit).grid(row=2, column=2)

t = Text(height=3, width=40)
t.grid(row=2, column=0, columnspan=2)
mainloop()
