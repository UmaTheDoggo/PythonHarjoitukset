import random

summa = 0
arpakuutiot = int(input("Arpakuutioiden lukumäärä: "))

for i in range (arpakuutiot):
    heitto = random.randint(1, 6)
    print(heitto)
    summa = summa + heitto
print(f"Noppien summa on: {summa}")