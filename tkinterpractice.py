import tkinter as tk

window = tk.Tk()
window.geometry('1920x1080')


intro = tk.Label(text="hello charlie nathan white")
intro["bg"] = "green"
intro["fg"] = "purple"
intro.place(x=40, y=30)

intro3 = tk.Label(text="hello mnty")
intro3["bg"] = "green"
intro3["fg"] = "purple"
intro3.grid(column=0, row=0)

intro2 = tk.Label(text="hello cameroon fein")
intro2["bg"] = "green"
intro2["fg"] = "purple"




window.mainloop()