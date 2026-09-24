# def tervehdi(kerrat):
#     for i in range(kerrat):
#         print("Hyvää päivää " + str(i+1) + ". kerran")

# print("Päivä alkaa tervehdyksellä")
# tervehdi(5)
# print("tervehditään lisää")
# tervehdi(2)

#--------------------------------------------------------------------
# def vaihda():
#     kaupunki = "Vantaa"
#     print("Funktiossa lopuksi: " + kaupunki)
#     return

# kaupunki = "Helsinki"
# print("Pääohjelmassa aluksi: " + kaupunki)
# vaihda()
# print("Pääohjelmassa lopuksi: " + kaupunki)

#----------------------------------------------------------------------

# def tervehdi(tervehdys, kerrat):
#     for i in range(kerrat):
#         print(tervehdys + " " + str(i+1) + ". kerran")
#     return

# tervehdi("Moi!", 3)
# tervehdi("Hyvää päivää", 2)
#----------------------------------------------------------------------

# def neliösumma(eka, toka):
#     ns = eka**2 + toka**2
#     return ns

# luku1 = float(input("Anna ensimmäinen luku: "))
# luku2 = float(input("Anna toinen luku: "))
# tulos = neliösumma(luku1, luku2)
# print(f"Lukujen {luku1:.3f} ja {luku2:.3f} neliösumma on {tulos:.3f}")
#----------------------------------------------------------------------


# def inventaario(tavarat):
#     print("Sinulla on seuraavat tavarat: ")
#     for t in tavarat:
#         print("- " + t)
#     return

# reppu = ["Vesipullo", "Kartta", "Kompassi"]
# inventaario(reppu)
# reppu.append("Linkkuveitsi")
# inventaario(reppu)
#------------------------------------------


def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat: ")
    for t in tavarat:
        print("- " + t)
    tavarat.clear()
    return

reppu = ["Vesipullo", "Kartta", "Kompassi"]
inventaario(reppu)
reppu.append("Linkkuveitsi")
inventaario(reppu)