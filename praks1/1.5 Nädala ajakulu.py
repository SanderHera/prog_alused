print("Sisestage ainepunktide arv: ")
ainepunkt = int(input())

print("Sisestage nädalate arv: ")
nädala_arv = int(input())

ajakulu = round((ainepunkt * 26) / nädala_arv, 2)

print(ajakulu)
