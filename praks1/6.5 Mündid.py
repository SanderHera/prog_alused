def pronksikarva_summa(raha):
    summa = 0
    for mündid in raha:
        if int(mündid) <= 5:
            summa += int(mündid)
        return summa
fail = open(input("Sisesta failinimi: "), encoding="UTF-8")
raha = []
for i in fail:
    raha.append(i[:-1])
print("Hoiupõrsasse läheb " + str(pronksikarva_summa(raha)) + " senti.")