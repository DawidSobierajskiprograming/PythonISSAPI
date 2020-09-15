import tkinter
from tkinter import *

window = tkinter.Tk()

window.title("GUI") 
def send_message():
    print("Hello World!")

label = tkinter.Label(window, text = "- GO FUCK YOUR SELF -").pack()

button_widget = Button(window, text = "Hello", command = send_message()).pack()

window.mainloop()
