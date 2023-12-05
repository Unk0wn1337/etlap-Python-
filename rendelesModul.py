def rendelesFelvetel():
    rendeltLista = []
    veglegesFizetesAr: int = 0
    kajaBekeres = int(input("Étel sorszáma: "))
    while not kajaBekeres == 0:
        if kajaBekeres == 1:
            rendeltLista.append("gazpacho")
            veglegesFizetesAr += 3000
        elif kajaBekeres == 2:
            rendeltLista.append("husleves")
            veglegesFizetesAr += 2500
        elif kajaBekeres == 3:
            rendeltLista.append("kremleves")
            veglegesFizetesAr += 4000
        elif kajaBekeres == 4:
            rendeltLista.append("sertesbelszin")
            veglegesFizetesAr += 3500
        elif kajaBekeres == 5:
            rendeltLista.append("lazacfile")
            veglegesFizetesAr += 6000
        elif kajaBekeres == 6:
            rendeltLista.append("gombas rizotto")
            veglegesFizetesAr += 4800
        elif kajaBekeres == 7:
            rendeltLista.append("csokoladetorta")
            veglegesFizetesAr += 3000
        elif kajaBekeres == 8:
            rendeltLista.append("citrusos panna")
            veglegesFizetesAr += 4700
        elif kajaBekeres == 9:
            rendeltLista.append("csokigolyo")
            veglegesFizetesAr += 7500
        kajaBekeres = int(input("Étel sorszáma: "))
    return veglegesFizetesAr

def rendelesModulMain():
    print("Üdvözöljük éttermünkben")
    vegAr = rendelesFelvetel()
    print(f"Végösszeg: {vegAr} ft")


