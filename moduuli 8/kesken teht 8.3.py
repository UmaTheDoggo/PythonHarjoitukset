while True:
    Lentoasema = input("Haluatko syöttää uuden lentoaseman, hakea jo haetun vai lopettaa: ").lower()

    if Lentoasema == "Uusi lentoasema":
       input("Kirjoita uusi lentoasema")

    if Lentoasema == "jo haettu":
        print("nönnönnöö")

    if Lentoasema == "lopeta":
        break



# lentokoodi = {"helsinki": "nönönöö", "vantaa": "nananaa"}
# if Lentoasema in lentokoodi:
#     print(f"Lentonimi: {Lentoasema} Paikka on: {lentokoodi}")