hyttiluokka = input("Anna hyttiluokka (LUX, A, B, C): ")

if hyttiluokka in ["LUX", "lux", "Lux"]:
    print("LUX on parvekkeellinen hytti yläkannella")

elif hyttiluokka in ["A", "a"]:
    print("A on ikkunallinen hytti autokannen yläpuolella")

elif hyttiluokka in ["B", "b"]:
    print("B on ikkunaton hytti autokannen yläpuolella.")

elif hyttiluokka in ["C", "c"]:
    print("C on ikkunaton hytti autokannen alapuolella")

else:
    print("Virheellinen hyttiluokka.")