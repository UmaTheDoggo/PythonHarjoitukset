import random

def noppa(tahkot):
    return random.randint(1, tahkot)

def main():
    maksimi = int(input("Syötä nopan tahkojen määrä: "))
    heitto = 0

    while heitto != maksimi:
        heitto = noppa(maksimi)
        print(f"Heiton Tulos: {heitto}")

if __name__ == "__main__":
    main()