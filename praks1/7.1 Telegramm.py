fail = open(input("Sisestage failinimi: "), encoding ="UTF-8")
sõnum = fail.read().upper().replace("Ä", "AE").replace("Õ", "OE").replace("Ö", "OE").replace("Ü", "UE")
print(sõnum)
fail.close