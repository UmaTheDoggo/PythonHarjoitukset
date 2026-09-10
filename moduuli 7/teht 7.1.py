import random

def noppa():
    return random.randint(1, 6)

while True:
    numero = noppa()
    print(numero)
    if numero == 6:
        break