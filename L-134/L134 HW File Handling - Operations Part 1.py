#open file and read its contents
file = open("L-134/hwsample.txt",'r')
print(file.read())
file.close()

#open file and read its beginning 8 characters
file = open("L-134/hwsample.txt",'r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

#append your name age in the file
file = open("L-134/sample.txt",'a')
file.write(" Hello.. my name is Darasimi")
file.close()