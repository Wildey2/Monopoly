import tkinter as tk
from tkinter import *
import random
import BW3
import time

root = Tk()  # Defining root for the rest of the program

# **********************************************************************************************************************
# Game Setup


gameC = tk.Canvas(root,width=500, height=506)  # This creates the game canvas so that images can be used in the GUI
gameC.pack(pady=10, padx=10)  # This puts a padding around the canvas so hat there is a border
gameC.config(bg="black")  # This changes the background colour to black so that the main image had a black border
board = tk.PhotoImage(file="monopoly-board.png")  # This tells the program what the file is (in the same folder)
board_img = gameC.create_image(252,255,image=board)  # This creates the image on the screen
redDot = tk.PhotoImage(file="red-dot.png")  # This imports the file for the red counter
P1 = gameC.create_image(450,490,image=redDot)  # This puts the image on the screen over GO
blueDot = tk.PhotoImage(file="blue-dot.png")  # This imports the file for the blue counter
Cpu = gameC.create_image(485,455,image=blueDot)  # This puts the blue counter image on the screen over GO
displayBox = Text(root)  # This creates the display box with the text
displayBox.pack(padx = 10)  # This adds a padding around the text boc so that it has a border
displayBox.insert(END,">>> Monopoly Game \n\n")  # This inputs on the first line so they know what the game is
displayBox.insert(END,"Welcome to Monopoly.")  # This introduces them to the game and then prompts them to pick a player mode
positionP1 = 0  # This creates the variable for position of the players
positionCpu = 0  # This creates

# **********************************************************************************************************************
# One player Function


def onePlayer():
    displayBox.insert(END,"You will be the red counter. The computer will be the blue  counter\n")
    #  Tells the user what counter they have been given

    displayBox.insert(END, "\nYou will now roll to start\n"
                           "Player one press r to roll\n\n")

# **********************************************************************************************************************
# Roll Player One Function


def rollP1(*args):

    root.bind("<y>",buy)


    global P1
    global positionP1

    dice1P1 = random.randint(1,6)
    dice2P1= random.randint(1,6)
    diceTotalP1 = dice1P1 + dice2P1
    positionP1 += diceTotalP1
    if positionP1 >= 40:
        positionP1 += -40

    displayBox.insert(END,"You rolled an " + str(diceTotalP1))
    if diceTotalP1 >= 10:
        displayBox.insert(END, "!\n\n")
    else:
        displayBox.insert(END, "\n\n")

    fileInP1Pos = open("positions.txt", "r")
    contentP1Pos = fileInP1Pos.read()  # Gets the entire file including \n and stores it as
    listP1Pos = BW3.generateList(contentP1Pos)

    movePositionP1 = listP1Pos[positionP1]
    listP1x = movePositionP1.split(",")
    xp1 = int(listP1x[0])
    yp1 = int(listP1x[1])

    gameC.delete(P1)
    P1 = gameC.create_image(xp1, yp1, image=redDot)

    fileInP1Name = open("names.txt", "r")
    contentP1Name = fileInP1Name.read()
    listP1Name = BW3.generateList(contentP1Name)
    print(listP1Name)

    fileInP1Money = open("cost.txt", "r")
    contentP1Money = fileInP1Money.read()
    listP1Money = BW3.generateList(contentP1Money)
    print(listP1Money)

    if listP1Name[positionP1] == "Chance":
        displayBox.insert(END,"You Landed on Chance")

    elif listP1Name[positionP1] == "Community Chest":
        displayBox.insert(END,"You Landed on Community Chest")

    elif listP1Name[positionP1] == "Jail/Visiting":
        displayBox.insert(END,"You are just passing through Jail")

    elif listP1Name[positionP1] == "Free Parking":
        displayBox.insert(END,"You are in free parking")

    elif listP1Name[positionP1] == "Go to Jail":
        displayBox.insert(END,"You will now go to Jail")

    else:
        displayBox.insert(END,"Would you like to buy the property " + listP1Name[positionP1] + " it will cost " + listP1Money[positionP1] +"$")

# **********************************************************************************************************************
#  Buy Function

    def buy(*args):

        displayBox.insert(END, "You Purchase " + movePositionP1 + " for " + listP1Money[positionP1])

# **********************************************************************************************************************
# Roll CPU Function

def rollCpu():

    global Cpu
    global positionCpu

    displayBox.insert(END,"The comuter will now roll!")

    dice1Cpu = random.randint(1,6)
    dice2Cpu = random.randint(1,6)
    diceTotalCpu = dice1Cpu + dice2Cpu
    positionCpu += diceTotalCpu
    if positionCpu >= 40:
        positionCpu += -40

    displayBox.insert(END,"The computer rolled a " + str(diceTotalCpu))
    if diceTotalCpu >= 10:
        displayBox.insert(END,"!\n\n")
    else:
        displayBox.insert(END,"\n\n")

    fileInCpu = open("positions.txt","r")
    contentCpu = fileInCpu.read()
    listCPu = BW3.generateList(contentCpu)

    movePositionCpu = listCPu[positionCpu]

    if movePositionCpu == "465,40":
        movePositionCpu = "40,465"


    listCPux = movePositionCpu.split(",")
    xCpu = int(listCPux[0])
    yCpu = int(listCPux[1])

    gameC.delete(Cpu)
    Cpu = gameC.create_image(xCpu,yCpu, image=blueDot)


#***********************************************************************************************************************

root.bind("<r>", rollP1)  # This binds the key R to the roll function

onePlayer()  # Calls the one player function

root.mainloop()
