for i in range (5):
    user = input("Kirjoita käyttäjätunnus: ")
    if user == "python":
        password = input("Kirjoita salasana: ")
        if password == "rules":
            print("Tervetuloa")
            break
        else:
            print("Väärä salasana")
    else:
        print("Väärä käyttäjätunnus")
else:
    print("Pääsy evätty")