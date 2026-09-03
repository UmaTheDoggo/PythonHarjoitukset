luku = int(input("Syötä luku: "))

if luku > 1:
    alkuluku = True

    for i in range(2, luku):
        if luku % i == 0:
            alkuluku = False
            break
    if alkuluku:
        print(f"luku: {luku} on alkuluku")
    else:
        print(f"luku: {luku} ei ole alkuluku")
else:
    print(f"luku: {luku} ei ole alkuluku")