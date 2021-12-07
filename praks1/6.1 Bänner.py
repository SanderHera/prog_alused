def banner(reklaamlause):
    return reklaamlause.upper()
korda = int(input("Mitu korda soovite reklaamlauset kuvada? "))
reklaamlause = input("Sisestage reklaamlause: ")
for i in range(0, korda):
    print(banner(reklaamlause))