import tkinter as tk
from tkinter import *

root = Tk()  # Defining root for the rest of the program


def run(*args):  # Defining run this will be executed when the enter key is pressed

    eboxval = eBox.get()  # This gets the input from the entry box that appears

    if eboxval == "1":  # This checks the entry box. If the entry is "1" then the one player function will be called
        eBox.pack_forget()  # This forgets the entry that has been taken and takes the box off of the screen
        onePlayer()  # Calling the one player function

    elif eboxval == "2":  # This checks the entry box. If the entry is "2" then the two player function will be called
        eBox.pack_forget()
        twoPlayer()  # Calling the two player function

    else:
        displayBox.insert(END, "***Input Invalid***")
        # If the input is not "1" or "2" then the Input Invalid will be will be printed to the screen


def onePlayer():
    displayBox.insert(END,"You have selected one player mode\n")  # Tells the user which game mode they have selected
    displayBox.insert(END,"You will be the red counter. The computer will be the blue counter")
    #  Tells the user what counter they have been given

    displayBox.config(state="disable")  # Disables the screen so that the user can not edit the info inside it


def twoPlayer():
    displayBox.insert(END,"You have selected two player mode\n")  # Tells the suer which game mode they have selected
    displayBox.insert(END, "Player one you will be the red counter. Player two will be the blue counter")
    #  Tells the user what counter they have been given

    displayBox.config(state="disable")  # Disabled the screen so that the user can not edit the info inside it


gameC = tk.Canvas(root,width=500, height=506)  # This creates the game canvas so that images can be used in the GUI
gameC.pack(pady=10, padx=10)  # This puts a padding around the canvas so hat there is a border
gameC.config(bg="black")  # This changes the background colour to black so that the main image had a black border
board = tk.PhotoImage(file="monopoly-board.png")  # This tells the program what the file is (in the same folder)
board_img = gameC.create_image(252,255,image=board)  # This creates the image on the screen
displayBox = Text(root)  # This creates the display box with the text
displayBox.pack(padx = 10)  # This adds a padding around the text boc so that it has a border
displayBox.insert(END,">>> Monopoly Game \n\n")  # This inputs on the first line so they know what the game is

displayBox.insert(END,"Welcome to Monopoly. Do you want to play 1 or 2 player?\n\n")
# This introduces them to the game and then prompts them to pick a player mode

eBox = Entry(root)  # This creates the entry box
eBox.pack()  # This adds the box to the screen and adds a boreder
eboxval = 0  # This declares the value of the box

root.bind("<Return>", run)  # This binds the key enter to the run function


root.mainloop()
