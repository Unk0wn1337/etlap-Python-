import etlapDesing

def kiiras():
    eloetelLista = ["gazpacho","husleves","kremleves"]
    eloetelListaAr = [3000, 2500, 4000]
    foetelLista = ["sertesbelszin","lazacfile","gombas rizotto"]
    foetelListaAr = [3500, 6000, 4800]
    desszertLista = ["csokoladetorta","citrusos panna","sozott csokigolyo"]
    desszertListaAr = [3000, 4700, 7500]

    etlapDesing.jel("*", 30)
    etlapDesing.etteremMegnevezes("Borsodi etterem")
    etlapDesing.jel("*", 30)

    etlapDesing.szovegKiiras("_" * 6, "Levesek", "_" * 6)
    print("")
    index = 0
    while index < len(eloetelLista):
        etlapDesing.etelekKiirasa(index+1,eloetelLista[index],eloetelListaAr[index])
        index+=1
    etlapDesing.szovegKiiras("_" * 6, "Foetel", "_" * 6)
    print("")
    index = 0
    while index < len(foetelLista):
        etlapDesing.etelekKiirasa(index+1,foetelLista[index],foetelListaAr[index])
        index+=1

    etlapDesing.szovegKiiras("_" * 6, "Desszertek", "_" * 6)
    print("")
    index = 0
    while index < len(desszertLista):
        etlapDesing.etelekKiirasa(index+1, foetelLista[index], foetelListaAr[index])
        index+=1
    etlapDesing.jel("_", 30)
    print("")