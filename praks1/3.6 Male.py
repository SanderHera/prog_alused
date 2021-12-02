taisarv = int(input("Sisestage täisarv: "))
i = 1
nisuteri = 0
if taisarv == 0:
    print("Nisuteri " + str(taisarv) + ".ruudu eest: " + str (nisuteri))
 elif taisarv > 64:
     print("Malelaual ei ole nii palju ruute")
 elif taisarv < 0:
     print("Malelaual ei saa olla negatiiv arv ruute")
 else:
     nisuteri = 1
     while i < taisarv:
         i += 1
         nisuteri *= 2
       print("Nisuteri " + str(taisarv) + ".ruudu eest: " + str (nisuter))
       