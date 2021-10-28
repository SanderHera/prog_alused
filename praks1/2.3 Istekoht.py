import random
koha_valik = str(input('Kas soovite istekohta ise valida ("ise") või loosida ("loos")? '))
ise_koht = " ";
if koha_valik == "ise":
    ise_koht = str(input('Kas soovite istuda akna ääres ("aken") või mitte ("muu")? '))
else:
    if random.randint(1, 3) == 1:
        print("Istekoht loositi. Aknakoht")
    else:
        print("Istekoht loositi. Vahekäigukoht")
if ise_koht == "aken":
    print("Valisite ise. Aknakoht")
elif ise_koht == "muu":
    print("Valisite ise. Vahekäigukoht")