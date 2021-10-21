inimesed = int(input("Sisesta inimeste arv: "))
kohad_bussis = int(input("Sisesta kohtade arv ühes bussis: "))
bussid = inimesed // kohad_bussis
maha_jäänud = inimesed % kohad_bussis
print(maha_jäänud)
