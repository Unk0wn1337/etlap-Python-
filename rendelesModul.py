def rendelesFelvetel(etelek):
    rendeltLista = []
    veglegesFizetesAr: int = 0
    print("Üdvözöljük éttermünkben")
    kajaBekeres = int(input("Étel sorszáma: "))
    while not kajaBekeres == 0:
            rendeltLista.append(etelek[kajaBekeres-1][0])
            veglegesFizetesAr += (etelek[kajaBekeres-1][1])
            kajaBekeres = int(input("Étel sorszáma: "))
    print(f"Végösszeg: {veglegesFizetesAr} ft")
    return veglegesFizetesAr




