kirja_suurus = float(input("Sisestage kirja suurus: "))
kirja_pealkiri = str(input("Sisestage kirja teema pealkiri: "))
kirja_manus = str(input("Kas kirjaga on kaasas fail (jah/ei)? "))
if kirja_pealkiri == "" or kirja_suurus > 1 and kirja_manus == "jah":
    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")
        
