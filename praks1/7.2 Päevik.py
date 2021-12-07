from datetime import *
päevik = open("paevik.txt", "a", encoding ="UTF-8")
kuupäev = datetime.today()
kiri = input("Sisesta sissekande tekst: ")
päevik.write(str(kuupäev) + "\n")
päevik.write(kiri + "\n")
päevik.close()