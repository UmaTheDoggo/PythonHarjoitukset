# while True:
#     bensa_maara = int(input("Bensan määrä galloneina: "))
#     print(f"Bensa litroina: {bensa_maara * 3.785}")

#     if bensa_maara < 0:
#         break
#
#
def gallona_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    gallonat = float(input("Anna bensiinin määrä gallonina: "))
    if gallonat < 0:
        break

    litrat = gallona_litroiksi(gallonat)
    print(f"{gallonat} gallonaa = {litrat:.2f} litraa")