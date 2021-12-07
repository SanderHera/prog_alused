ring = int(input("Sisesta ringide arv: "))
ring += 1
porgandid = 0
for i in range(2, ring, 2):
    porgandid += i
print("Porgandite kogu arv on " + str(porgandid) + ".")
