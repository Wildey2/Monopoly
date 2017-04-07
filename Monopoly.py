import time
from tkinter import *




def run(*args):

    ''''''

root = Tk()

displayBox = Text(root)
displayBox.pack(padx = 10, pady = 10)
displayBox.insert(END,">>> Monopoly Game \n\n")

def blink():
    root.after(1000, displayBox.insert(END,".\n\n"))

blink()


displayBox.insert(END,"Welcome to Monopoly. Do you want to play 1 or 2 player?\n\n")









root.mainloop()