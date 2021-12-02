from tkinter import *
raam = Tk()
raam.title("Aseri valla lipp")
tahvel = Canvas(raam, width = 900, height = 600)
tahvel.create_rectangle(0, 0, 900, 250, fill="dark blue", outline="dark blue")
tahvel.create_rectangle(0, 250, 900, 350, fill="white", outline="white")
tahvel.create_rectangle(0, 350, 900, 600, fill="green", outline="green")
tahvel.pack()
raam.mainloop()