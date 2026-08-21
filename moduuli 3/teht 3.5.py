lieviskät = float(input("Syötä lieviskät: "))
naulat = float(input("Syötä naulat: "))
luodit = float(input("Syötä luodit: "))

#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.
#massa = lieviskät * 20 * 32 * 13.3 + naulat * 32 * 13.3 + luodit * 13.3 ilmoita kokonaislukuna
print(f"Massa on {int((lieviskät * 20 * 32 * 13.3 + naulat * 32 * 13.3 + luodit * 13.3) / 1000)} kilogrammaa.")
print(f"Massa on {int((lieviskät * 20 * 32 * 13.3 + naulat * 32 * 13.3 + luodit * 13.3) % 1000)} grammaa.")