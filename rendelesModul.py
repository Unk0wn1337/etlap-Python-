veglegesFizetesAr: int = 0


def rendelesModulMain():
    global veglegesFizetesAr
    print("Udvozoljuk az etteremben")
    levesek()


def levesek():
    global veglegesFizetesAr
    levesKerdes: str = input("Szeretne kerni levest? (I/N) ")
    if levesKerdes == "I" or levesKerdes == "i":
        levesMegnevezes: str = input("Milyen levest szeretne? valasszon a fenti listabol: ")
        if levesMegnevezes == "gazpacho":
            veglegesFizetesAr += 3000
            print("gazpacho hozzaadva")
            foEtel()
        elif levesMegnevezes == "husleves":
            veglegesFizetesAr += 2500
            print("husleves hozzaadva")
            foEtel()
        elif levesMegnevezes == "kremleves":
            veglegesFizetesAr += 2250
            print("kremleves hozzaadva")
            foEtel()
        else:
            print("Ilyen leves nincsen ami ettermunkben")
            levesek()
    elif levesKerdes == "N" or levesKerdes == "n":
        foEtel()
    else:
        print("HIBA: Csak I-vel vagy N-el lehet valaszolni a kerdesekre!")


def foEtel():
    global veglegesFizetesAr
    foEtelKerdes: str = input("Szeretne kerni foetelt? (I/N) ")
    if foEtelKerdes == "I" or foEtelKerdes == "i":
        foEtelMegnevezes: str = input("Milyen foetelt szeretne? valassszon a fenti listabol: ")
        if foEtelMegnevezes == "sertesbelszin":
            veglegesFizetesAr += 3500
            print("sertesbelszin hozzaadva")
            desszert()
        elif foEtelMegnevezes == "lazacfile":
            veglegesFizetesAr += 6000
            print("lazacfile hozzadva")
            desszert()
        elif foEtelMegnevezes == "gombas rizotto":
            veglegesFizetesAr += 4800
            print("gombas rizotto hozzadva")
            desszert()
        else:
            print("Mas etelunk nincsen sajnos, amire te gondolsz")
            foEtel()
    elif foEtelKerdes == "N" or foEtelKerdes == "n":
        desszert()
    else:
        print("HIBA: Csak I-vel illetve N-el lehet valaszolni!")


def desszert():
    global veglegesFizetesAr
    desszertKerdes: str = input("Szeretne kerni desszertet? (I/N) ")
    if desszertKerdes == "I" or desszertKerdes == "i":
        desszertMegnevezes: str = input("Milyen desszertet szeretne? valasszon a fenti listabol: ")
        if desszertMegnevezes == "csokoladetorta":
            veglegesFizetesAr += 3000
            print("csokoldaetorta hozzadva")
            vegOsszeg()
        elif desszertMegnevezes == "citrusos panna":
            veglegesFizetesAr += 4700
            print("citrusos panna hozzadva")
            vegOsszeg()
        elif desszertMegnevezes == "sozott csokigolyo":
            veglegesFizetesAr += 7500
            print("Sef bacsi sozott csokigolyoi hozzadva")
            vegOsszeg()
        else:
            print("Mas desszertunk nincsen sajnos amire te gondolsz")
            desszert()
    elif desszertKerdes == "n" or desszertKerdes == "N":
        vegOsszeg()
    else:
        print("HIBA: Csak I-vel illetve N-el lehet valaszolni!")


def vegOsszeg():
    global veglegesFizetesAr
    print(f"Koszonjuk, hogy nalunk vasarolt a teljes ar: {veglegesFizetesAr}ft")
