import tkinter as tk

def LOLXDSKAMMED():
    sigm = tk.Label(text="LOLXDSKAMMED")
    sigm["bg"] = "blue"
    sigm["fg"] = "white"
    sigm.grid(column=2, row=1)

window = tk.Tk()
window.geometry('400x400')
sig = tk.Label(text="Welcome to my amazing program")

sig["bg"] = "blue"
sig["fg"] = "white"
sig.grid(column=0, row=0)

clickbutton = tk.Button(text="press for free VBUCKS",command=LOLXDSKAMMED)
clickbutton.grid(row=0, column=2)

window.mainloop()

