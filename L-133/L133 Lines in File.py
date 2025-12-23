# Program to count number of lines in this file
# Openinga file
file = open("L-133/hello.txt","r")
Counter = 0

# Reading from file
Content = file.read()
# splitting content into lines
# and storing them ina list
CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1

print("This is number of lines in file")
print(Counter)