sukupuoli = input("Kerro biologinen sukupuolesi:")
hemogoblini = float(input("kerro hemoglobiiniarvo:"))

if sukupuoli.lower() in ["nainen", "tyttö"]:
    if hemogoblini < 117:
        print("Hemoglobiiniarvo on alhainen")
    elif hemogoblini > 175:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on normaali")

if sukupuoli.lower() in ["mies", "poika"]:
    if hemogoblini < 135:
        print("Hemoglobiiniarvo on alhainen")
    elif hemogoblini > 195:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on normaali")
        
