import tkinter
from tkinter import *
from tkinter import messagebox
from ISSAPI import *

window = tkinter.Tk()
img = PhotoImage(file='ISSimage.gif')
window.title("GUI")

def send_message1():
    messagebox.showinfo("ISS altitude", "The ISS is " + getaltitude() + " Kilometers above sea level")

def send_message2():
    messagebox.showinfo("ISS velocity", "The ISS is traveling at " + getvelocity() + " Kph")

def send_message3():
    messagebox.showinfo("ISS latitude and Longitude", "The ISS is at Latitude " + getlatitude() + "° N, Longitude " + getlongitude() + "° E" )


ISSimage = Canvas(window, width = 720, height = 400)
ISSimage.pack()
ISSimage.create_image(20,20, anchor = NW, image = img)
ISSimage.pack()

label = tkinter.Label(window, text = "- This is The ISS info App -").pack()
label2 = tkinter.Label(window, text = "- What would you like to know about the ISS at this moment -").pack()

button_widget = Button(window, text = "Altitude", command = send_message1).pack(side=LEFT, padx=10)
button_widget = Button(window, text = "Velocity", command = send_message2).pack(side=LEFT, padx=10)
button_widget = Button(window, text = "Latitude and longitude", command = send_message3).pack(side=LEFT, padx=10)

window.mainloop()
