# Kysy kuukauden numero
vuodenajat = ("talvi", "kevät", "kesä", "syksy")
kuukausi = int(input("Mones kuukausi on (1-12): "))

#12-2 on talvi, 3-5 kevät 6-8 on kesä 9-11 on syksy 
vuodenaika = vuodenajat[kuukausi % 12 // 3]
print(f"{kuukausi}. kuukausi on {vuodenaika}")