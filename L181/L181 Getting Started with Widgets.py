from tkinter import *
from datetime import date

# create Window
window = Tk()
window.title("Getting Started with Widgets")
window.geometry("400x300")

def display(): # Function to display a Message
    name = name_entry.get()

    # Declaring a global variable
    # to make it accessible anywhere in program
    global Message
    Message = "Welcome to the Application! \nToday's date is:"
    greet = "Hello "+name+"\n"

    # Display details in a text box
    # Specify where to add the details inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())

# Create widgets
label = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=300)

name_label = Label(text="Enter your full Name below", bg="blue", fg="white")
name_entry = Entry() #text input

text_box = Text(height=3)

btn = Button(text="Display message", command=display, height=1, bg="red", fg="white")

# Attaching all the Widegets in the window
label.pack()
name_label.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()