nimet = set()

while True:
    nimi = input("Kirjoita nimi (tyhjä lopettaa): ")
    
    if nimi == "":
        break
    
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print(f"Nimet: {nimet}")