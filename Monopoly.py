import time
from tkinter import *




def run(*args):

    ''''''

root = Tk()

def onePlayer():
    displayBox.insert(END,"You have selected one player mode")


def twoPlayer():
    displayBox.insert(END,"You have selected two player mode")

displayBox = Text(root)
displayBox.pack(padx = 10, pady = 10)
displayBox.insert(END,">>> Monopoly Game \n\n")

displayBox.insert(END,"Welcome to Monopoly. Do you want to play 1 or 2 player?\n\n")

eBox = Entry(root)
eboxval = eBox.get()
eBox.pack()

if eboxval == "1":
    onePlayer()

elif eboxval == "2":
    twoPlayer()

else:
    displayBox.insert(END,"***Input Invalid***")









root.mainloop()
