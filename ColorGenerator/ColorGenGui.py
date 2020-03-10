import random
from tkinter import *

file = open('ColorGenerator/PGNouns.txt', 'r')
noun = file.readlines()
file.close()
file = open('ColorGenerator/Colors.txt', 'r')
color = file.readlines()
file.close()


def gen():
    print(noun[random.randint(0, len(noun)-1)])
    print(color[random.randint(0, len(color)-1)])


mainWindow = Tk()
mainWindow.geometry("200x200")
mainWindowTitle = Label(mainWindow, text="ColorGen V1")
b = Button(mainWindow, text="Generate Another", command=gen)
b.place(x=30, y=20)
nound = Label(mainWindow, text="Oops There")
colord = Label(mainWindow, text="Was an Error")
mainWindowTitle.pack()
mainWindow.mainloop()
