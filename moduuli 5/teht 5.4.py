import random
konenumero = random.randint(1, 10)

while True: 
    luku = float(input("Anna numero: "))

    if konenumero < luku:
        print("Liian suuri arvaus")

    elif konenumero > luku:
        print("Liian pieni arvaus")

    elif konenumero == luku:
        print("Oikein arvattu!")
        break