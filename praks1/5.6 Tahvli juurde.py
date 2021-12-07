from datetime import *
fail = open (input("Sisestage failinimi: "), encoding="UTF-8")
nimekiri = []
for nimi in fail:
    nimekiri.append(nimi)
print("Vastama tuleb: " + str(nimekiri[int(datetime.now().day) - 1]))
fail.close()