def mahlapakkide_arv(õun):
    mahlapakkide_arv = round(õun*0.4/3)
    return mahlapakkide_arv
õun = float(input("Mitu kilogrammi õunu on? "))
print(str(õun) + " kilogrammi õunte eest saab " + str(mahlapakkide_arv(õun)) + " mahlapakki")
