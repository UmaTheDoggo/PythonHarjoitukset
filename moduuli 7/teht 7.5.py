lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

def parilliset(luvut):
    for luku in luvut:
        if luku % 2 == 0:
            print(luku)

parilliset(lista)