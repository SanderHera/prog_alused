def tervitus(kord):
    print("""Võõrustaja: "Tere!" """)
    print("Täna " + str(kord) + ". kord tervitada, mõtiskleb võõrustaja.")
    print("""Külaline: "Tere, suur tänu kutse eest!" """)
kord = int(input("Sisestage külalise arv:"))
for i in range(1 , kord + 1):
    tervitus(i)