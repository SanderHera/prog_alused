def eelarve(külalised):
    rent = 55
    summa = külalised * 10 + rent
    return summa
kutsutud = int(input("Mitu inimest on kutsutud? "))
tuleb = int(input("Mitu inimest tuleb? "))
print("Maksimaalne eelarve: " + str(eelarve(kutsutud)) + " eurot")
print("Minimaalne eelarve: " + str(eelarve(tuleb)) + " eurot")