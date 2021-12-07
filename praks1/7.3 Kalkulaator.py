from easygui import *
x = enterbox("Sisestage esimene täisarv lõigus 1-10:")
y = enterbox("Sisestage teine täisarv lõigus 1-10:")
märgid = ["+","-","*"]
märk = buttonbox("Valige tehte märk", choices = märgid)
if märk == "+":
    vastus = int(x) + int(y)
elif märk == "-":
    vastus = int(X) - int(y)
elif märk == "*":
    vastus = int(x) * int(y)
msgbox("Tehte tulemus on " + str(vastus))
