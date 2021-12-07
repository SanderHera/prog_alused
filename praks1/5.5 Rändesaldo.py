fail = open ("sisseranne.txt", encoding="UTF-8")
sisseränneloend = []
for ränne in fail:
    sisseränneloend.append(ränne)
fail.close()
fail = open ("valjaranne.txt", encoding="UTF-8")
väljaränneloend = []
for ränne in fail:
    väljaränneloend.append(ränne)
fail.close()
rändesaldoloend = []
i = 0
while i < 10:
    rändesaldoloend.append(int(sisseränneloend[i]) - int(väljaränneloend[i]))
    i += 1
print(rändesaldoloend)
if max(rändesaldoloend) > 0:
    print("Suurim positiivne rändesaldo oli " + str(i) +". aastal.")
else:
    print("Positiivse rändesaldoga aastaid ei ole.")
