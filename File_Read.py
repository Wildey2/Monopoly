import BW3

fileIn = open("positions.txt","r")

content = fileIn.read()  # Gets the entire file including \n and stores it as

list = BW3.generateList(content)

print(list)




