import tkinter
from tkinter import *
from tkinter import messagebox
from ISSAPI import getaltitude

window = tkinter.Tk()
img = PhotoImage(file='ISSimage.gif')
window.title("GUI")

def send_message():
    messagebox.showinfo("ISS altitude", "The ISS is " + getaltitude() + " Kilometers above sea level")

ISSimage = Canvas(window, width = 720, height = 400)
ISSimage.pack()
ISSimage.create_image(20,20, anchor = NW, image = img)
ISSimage.pack()

label = tkinter.Label(window, text = "- This is The ISS info App -").pack()
label2 = tkinter.Label(window, text = "- What would you like to know about the ISS at this moment -").pack()

button_widget = Button(window, text = "Altitude", command = send_message).pack(side=LEFT, padx=10)
button_widget = Button(window, text = "Hello", command = send_message).pack(side=LEFT, padx=10)

window.mainloop()
