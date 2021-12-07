fail = str(input("Palun sisestage failinimi valikus on jukebox, 80ndad, eesti_muusika, edm: "))
if fail.endswith(".txt") == False:
    fail = fail + ".txt"
fail = open(fail, encoding="UTF-8")
mitmespala = 1
print("Muusikapalade valik:")
loend = []
for rida in fail:
    print(str(mitmespala) + ". " + str(rida[:-1]))
    mitmespala += 1
    loend.append(rida)
lauluvalik = int(input("Valige laulu järjekorranumber: "))
lauluvalik -= 1
print("Mängitav muusikapala on " + loend[lauluvalik])
fail.close()