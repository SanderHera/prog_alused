def eelarve(külalised):
    rent = 55
    summa = külalised * 10 + rent
    return summa
fail = open(input("Sisesta failinimi: "), encoding="UTF-8")
tuleb = 0
ei_tule = 0
for rida in fail:
    if rida.startswith("+") == True:
        tuleb += 1
    else:
        ei_tule += 1
print("Kutsutud on " + str(tuleb + ei_tule) + " eurot")
print("peole tuleb " + str(tuleb) + " inimest")
print("Maksimaalne eelarve: " + str(eelarve(tuleb + ei_tule)) + " eurot")
print("Minimaalne eelarve: " + str(eelarve(tuleb)) + " eurot")