import tkinter as tk
from tkinter import *

upgrade = 1
click = 0
def cookie1():
    global click
    global upgrade
    click += (upgrade*1)
    print(click)
    sigm = tk.Label(text="you have "+ str(click) +" cookies")
    sigm["bg"] = "blue"
    sigm["fg"] = "white"
    sigm.place(relx=0.5, rely=0.2, anchor="center")
    
def cookie2():
    global upgrade
    global click
    if click >= 50:
        upgrade += 1 
        click = click -50
        sigm = tk.Label(text="you have "+ str(click) +" cookies")
        sigm["bg"] = "blue"
        sigm["fg"] = "white"
        sigm.place(relx=0.5, rely=0.2, anchor="center")

window = tk.Tk()
window.geometry('1920x1080')
sig = tk.Label(text="cookie clicker")
PhotoImage = tk.PhotoImage(file="cookie clicker/images/cookie1.png")

sig["bg"] = "brown"
sig["fg"] = "white"
sig.grid(column=0, row=0)

clickbutton = tk.Button(image=PhotoImage,command=cookie1)
clickbutton.place(relx=0.5, rely=0.5, anchor="center")

clicking2 = tk.Button(text="upgrade for 50",command=cookie2)
clicking2.place(relx=0.5, rely=0.7, anchor="center")




window.mainloop()