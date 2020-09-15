import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
img = PhotoImage(file='ISSimage.gif')
window.title("GUI")

def send_message():
    messagebox.showinfo("Hello Python!", "Hello World!")

ISSimage = Canvas(window, width = 680, height = 423)
ISSimage.pack()
ISSimage.create_image(20,20, anchor = NW, image = img)
ISSimage.pack()

label = tkinter.Label(window, text = "- GO FUCK YOUR SELF -").pack()

button_widget = Button(window, text = "Hello", command = send_message).pack()

window.mainloop()
