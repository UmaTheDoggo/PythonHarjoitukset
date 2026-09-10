def pizza_halkasija(halkasija, hinta):
    radius = (halkasija / 2) /100
    area = 3.14 * (radius)
    return hinta / area

if __name__ == "__main__":
    print("Ensimmäinen pizza:")
    halkasija1 = float(input("Anna pizzan halkasija cm: "))
    hinta1 = float(input("Anna pizzan hinta: "))

    print("Toinen Pizza:")
    halkasija2 = float(input("Anna pizzan halkasija cm: "))
    hinta2 = float(input("Anna pizzan hinta: "))

    pizza_hinta1 = pizza_halkasija(halkasija1, hinta1)
    pizza_hinta2 = pizza_halkasija(halkasija2, hinta2)

    print(f"pizzan yksikköhinta: {pizza_hinta1:.2f} €/m^2")
    print(f"pizzan yksikköhinta: {pizza_hinta2:.2f} €/m^2")

    if pizza_hinta1 < pizza_hinta2:
        print("Ensimmäinen pizza antaa parempaa vastinetta rahalle")

    elif pizza_hinta1 > pizza_hinta2:
        print("Toinen pizza antaa parempaa vastinetta rahalle")

    else:
        print("Pizzat ovat saman arvoisia")