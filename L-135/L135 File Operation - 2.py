#create a new file
new_file = open("L-135/new-sample.txt", 'x')
new_file.close()

#check if a file exists
import os

print("Checking if my_file exists or not....")

if os.path.exists("L-135/sample.txt"):
    os.remove("L-135/sample.txt")
else:
    print("The file doesnot exists")

#create a new if it doesn't
my_file = open("L-135/sample.txt", "w")
my_file.write("Hi I am Darasimi and I am 10 year old")
my_file.close()

#delete file named sample
os.remove("L-135/sample.txt")

#delete the folder
os.rmdir('Folder')