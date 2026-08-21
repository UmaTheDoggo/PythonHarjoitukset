# Tehtävä 3.2 Ympyrän pinta-ala

#float muuntaa syötteen liukuluvuksi
radius = float(input("Syötä ympyrän säde: "))
area = 3.14 * radius ** 2

#print tulostaa tekstin näytölle ja funktiolla .2f pyöristetään luku kahden desimaalin tarkkuuteen
print(f"Ympyrän pinta-ala on {area:.2f}")