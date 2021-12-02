ringide_arv = int(input("Sisesta ringide arv: "))
i = 1
a = 0
porgandite_arv = 0
while i < ringide_arv:
    i = i + 2
    porgandite_arv = porgandite_arv + 2 + a
    a = a + 2
print("Porgandite koguarv on " + str(porgandite_arv) + ".")   
    
