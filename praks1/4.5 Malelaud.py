from tkinter import *
raam = Tk()
raam.title("Malelaud")
tahvel = Canvas(raam, width = 800, height = 800,)
x1 = 0
y1 = 0
x2 = 100
y2 = 100
i = 0
j = 1
while y2 <= 800:
    while x2 <= 800:
        if i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
            tahvel.create_rectangle(x1, y1, x2, y2, fill = "white", outline="white", )
        if i == 1 or i == 3 or i == 5 or i == 7:
            tahvel.create_rectangle(x1, y1, x2, y2, fill = "black", outline="black", )
        i += 1
        x1 += 100
        x2 += 100
    y1 += 0
    y2 += 100
    x1 += 0
    x2 += 100
    if j == 0 or j == 2 or j == 4 or j == 6:
        i = 0
    if j == 1 or j == 3 or j == 5 or j == 7:
        i = 1
    j += 1

tahvel.pack()
raam.mainloop()