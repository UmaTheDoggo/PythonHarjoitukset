tuuma = float(input("Anna tuumien määrä: "))
while tuuma > 0:
    print(f"Sentit: {tuuma * 2.54}")
    tuuma = float(input("Anna tuumien määrä: "))

if tuuma < 0:
    print("Sinut on vapautettu")

