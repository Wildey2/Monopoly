import tkinter as tk
from tkinter import *
import random
import BW3
import time


class App():


    def __init__(self):


        self.root = Tk()  # Defining root for the rest of the program

        # **********************************************************************************************************************
        # Game Setup

        self.moneyP1 = 1500
        self.gameC = tk.Canvas(self.root,width=500, height=506)  # This creates the game canvas so that images can be used in the GUI
        self.gameC.grid(column=1,row=0)  # This puts a padding around the canvas so hat there is a border
        self.gameC.config(bg="black")  # This changes the background colour to black so that the main image had a black border
        self.board = tk.PhotoImage(file="monopoly-board.png")  # This tells the program what the file is (in the same folder)
        self.board_img = self.gameC.create_image(252,255,image=self.board)  # This creates the image on the screen
        self.redDot = tk.PhotoImage(file="red-dot.png")  # This imports the file for the red counter
        self.P1 = self.gameC.create_image(450,490,image=self.redDot)  # This puts the image on the screen over GO
        self.blueDot = tk.PhotoImage(file="blue-dot.png")  # This imports the file for the blue counter
        self.Cpu = self.gameC.create_image(485,455,image=self.blueDot)  # This puts the blue counter image on the screen over GO
        self.displayBox = Text(self.root)  # This creates the display box with the text
        self.displayBox.grid(column=1,row=2)  # This adds a padding around the text boc so that it has a border

        self.displayBox.insert(END,"What is your name?\n Press Enter\n\n")
        self.name = Entry(self.root)
        self.name.grid(column=0, row=3)


        self.root.bind("<Return>",self.nameRun)


        self.moneyBoxLP1 = Label(self.root, text="P1 Money")  # Creates the label for P1 money
        self.moneyBoxLP1.grid(column=0, row=0, columnspan=1)  # Applies the label to the grid
        self.moneyBoxMP1 = Label(self.root, text=str(self.moneyP1))  # Creates the label for the money factor
        self.moneyBoxMP1.grid(column=0, row=1, columnspan=1)  # Applies the label to the grid
        self.moneyBoxLCpu = Label(self.root, text="Cpu Money")  # Creates the label for CPU Money
        self.moneyBoxLCpu.grid(column=3, row=0, columnspan=1)  # Applies the lablel to the grid
        self.moneyBoxMCpu = Label(self.root, text=str(self.moneyP1))  # Creates the label for the money factor
        self.moneyBoxMCpu.grid(column=3, row=1, columnspan=1)  # Applies the label to the grid
        self.root.title("Monopoly Game")

        self.root.mainloop()

    def nameRun(self,*args):


        self.nameVal = self.name.get()  # Getting the input from the text box when the enter key is pressed

        self.called = self.nameVal  # storing the name value due to prior error

        self.fileInP1Player = open("playernames.txt","r")  # Reading the player name into the player names file
        self.contentP1Name = self.fileInP1Player
        self.listP1Player = BW3.generateList(self.contentP1Name)

        # Making an alredy played name check system

        '''
        self.p1Called = ""
        self.ctr = 0
        for i in range(len(self.listP1Player)):
            if self.listP1Player ==
        '''



        self.fileIn = open("playernames.txt", "a") # Writing the player name into the player names file
        self.fileIn.write(self.called + ":")

        self.name.destroy()  # Deleting the input box from the screen

        self.displayBox.insert(END,"Welcome to Monopoly " + self.nameVal + ".")  # This introduces them to the game and then prompts them to pick a player mode
        self.positionP1 = 0  # This creates the variable for position of the players
        self.positionCpu = 0  # This creates the variable for position of the CPU

        self.root.bind("<r>", self.rollP1)  # This binds the key R to the roll function

        self.onePlayer()  # Calls the one player function


    # *********************************************************************************************************************
    # One player Function


    def onePlayer(self):
        self.displayBox.insert(END," You will be the red counter. The computer will be the  blue counter\n")  # Introduces the player to the game
        #  Tells the user what counter they have been given

        self.displayBox.insert(END, "\nYou will now roll to start\n"
                                    "Player one press r to roll\n\n")
        # Tells the user what they will have to do to roll the dice

    # **********************************************************************************************************************
    # Roll Player One Function


    def rollP1(self,*args):

        self.moneyP1 = 1500  # Sets player 1's money to the standard 1500

        self.dice1P1 = random.randint(1,6)  # This simulates a dice roll
        self.dice2P1= random.randint(1,6)
        self.diceTotalP1 = self.dice1P1 + self.dice2P1
        self.positionP1 += self.diceTotalP1
        if self.positionP1 >= 40:  # Keeping the limit to 40 (the # of spaces on the board)
            self.positionP1 += -40

        self.displayBox.insert(END,"You rolled an " + str(self.diceTotalP1))  # Telling the player what they rolled
        if self.diceTotalP1 >= 10:
           self. displayBox.insert(END, "!\n\n")  # If the player rolls higher than a 10 an ! mark gets put after the text
        else:
            self.displayBox.insert(END, "\n\n")

        self.fileInP1Pos = open("positions.txt", "r")
        self.contentP1Pos = self.fileInP1Pos.read()
        self.listP1Pos = BW3.generateList(self.contentP1Pos)    # Reads from the positions file

        self.movePositionP1 = self.listP1Pos[self.positionP1]
        self.listP1x = self.movePositionP1.split(",")
        self.xp1 = int(self.listP1x[0])
        self.yp1 = int(self.listP1x[1])

        self.gameC.delete(self.P1)
        self.P1 = self.gameC.create_image(self.xp1, self.yp1, image=self.redDot)  # Inserts the possitions in as co-ordinates

        self.fileInP1Name = open("names.txt", "r")  # Reading from the place names file
        self.contentP1Name = self.fileInP1Name.read()
        self.listP1Name = BW3.generateList(self.contentP1Name)


        self.fileInP1Money = open("cost.txt", "r")  # Reading from the cost file
        self.contentP1Money = self.fileInP1Money.read()
        self.listP1Money = BW3.generateList(self.contentP1Money)

        print(self.positionP1)  # Printing the two positions to the console
        print(self.listP1Name)

        # making all the exeptions for places which arent land

        if self.listP1Name[self.positionP1] == "Chance":
            self.displayBox.insert(END,"You Landed on Chance\n\n")
            rollCPu()

        elif self.listP1Name[self.positionP1] == "Community Chest":
            self.displayBox.insert(END,"You Landed on Community Chest\n\n")
            rollCPu()

        elif self.listP1Name[self.positionP1] == "Jail/Visiting":
            self.displayBox.insert(END,"You are just passing through Jail\n\n")
            rollCPu()

        elif self.listP1Name[self.positionP1] == "Free Parking":
           self. displayBox.insert(END,"You are in free parking\n\n")
           rollCPu()

        elif self.listP1Name[self.positionP1] == "Go to Jail":
            self.displayBox.insert(END,"You will now go to Jail\n\n")
            rollCPu()

        elif self.listP1Name[self.positionP1] == "Income Tax":
            self.displayBox.insert(END,"You Landed on income tax. You will be charged $200\n\n")
            self.moneyP1 += -200

            print(self.moneyP1)
            rollCPu()

        # Otherwise asking them if they would like to buy the property that they had landed on

        else:

            # Impliment check to see if the place has already been purchased

            self.displayBox.insert(END,"Would you like to buy the property " + self.listP1Name[self.positionP1] + " it will cost " + self.listP1Money[self.positionP1] +"$\n\n")

            self.eBox = Entry(self.root)
            self.eBox.grid(column=1,row=3)

            self.root.bind("<Return>", self.eBoxValRun)


    def eBoxValRun(self,*args):

        # Buying the place for the user

        self.eBoxVal = self.eBox.get()

        if self.eBoxVal == "Yes":

            self.purchasedFile = open("purchasedFile.txt","a")

            self.purchasedFile.write(self.listP1Name[self.positionP1]+"Purchased:")

            buy()

        elif self.eBoxVal == "No":

            self.displayBox.insert(END,"You don't buy the property")


        self.eBox.destroy()

        self.rollCpu()
    # **********************************************************************************************************************
    #  Buy Function

    def buy(self,*args):

        # Telling them what they bought

        self.displayBox.insert(END, "You Purchased " + self.movePositionP1 + " for " + self.listP1Money[self.positionP1])

    # **********************************************************************************************************************
    # Roll CPU Function

    def rollCpu(self):

        global Cpu
        global positionCpu

        self.displayBox.insert(END,"The comuter will now roll!")

        self.dice1Cpu = random.randint(1,6)
        self.dice2Cpu = random.randint(1,6)
        self.diceTotalCpu = self.dice1Cpu + self.dice2Cpu
        self.positionCpu += self.diceTotalCpu
        if self.positionCpu >= 40:
            self.positionCpu += -40

        self.displayBox.insert(END,"The computer rolled a " + str(self.diceTotalCpu))
        if self.diceTotalCpu >= 10:
            self.displayBox.insert(END,"!\n\n")
        else:
            self.displayBox.insert(END,"\n\n")


        self.fileInCpu = open("positions.txt","r")
        self.contentCpu = self.fileInCpu.read()
        self.listCPu = BW3.generateList(self.contentCpu)


        self.movePositionCpu = self.listCPu[self.positionCpu]

        if self.movePositionCpu == "465,40":
            self.movePositionCpu = "40,465"

        self.movePositionCpu = self.listCPu[self.positionCpu]
        self.listCPux = self.movePositionCpu.split(",")
        self.xCpu = int(self.listCPux[0])
        self.yCpu = int(self.listCPux[1])

        self.gameC.delete(self.Cpu)
        self.P1 = self.gameC.create_image(self.xCpu, self.yCpu, image=self.blueDot)


    # **********************************************************************************************************************

app = App()