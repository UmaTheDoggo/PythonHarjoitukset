luvut = []

while True:
    luku = input("Anna Luku: ")
    if luku == "":
        break

    luvut.append(int(luku))
print("pienin luku: ", min(luvut))
print("suurin luku: ", max(luvut))
