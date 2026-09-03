luvut = []

while True:
    numerot = input("Syötä numerot: ")
    if numerot == " ":
        break
    luvut.append(int(numerot))

vaihto = sorted(luvut, reverse=True)

for luku in vaihto[:5]:
    print(luku)