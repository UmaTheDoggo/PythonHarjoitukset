lentokoodi = {"helsinki": "nönönöö", "vantaa": "nananaa"}

Lentoasema = input("Haluatko syöttää uuden lentoaseman?: ")


if Lentoasema in lentokoodi:
    print(f"Lentonimi: {Lentoasema} Paikka on: {lentokoodi}")