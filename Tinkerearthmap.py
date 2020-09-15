import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()

window.title("GUI")

def send_message():
    messagebox.showinfo("Hello Python!", "Hello World!")

label = tkinter.Label(window, text = "- GO FUCK YOUR SELF -").pack()

button_widget = Button(window, text = "Hello", command = send_message).pack()

window.mainloop()
