import etlapDesing

def kiiras():
    etelek = [
        ("gazpacho", 3000),
        ("husleves", 2500),
        ("kremleves", 4000),
        ("sertesbelszin", 3500),
        ("lazacfile", 6000),
        ("gombas rizottto", 4800),
        ("csokoladetorta", 3000),
        ("citrusos panna", 4700),
        ("csokigolyo", 7500)
    ]


    etlapDesing.jel("*", 30)
    etlapDesing.etteremMegnevezes("Borsodi etterem")
    etlapDesing.jel("*", 30)

    etlapDesing.szovegKiiras("_" * 6, "Levesek", "_" * 6)
    print("")
    index = 0
    while index < len(etelek):
        etlapDesing.etelekKiirasa(index+1,etelek[index][0],etelek[index][1])
        if index == 2:
            break
        index+=1
    etlapDesing.szovegKiiras("_" * 6, "Foetel", "_" * 6)
    print("")
    index = 3
    while index < len(etelek):
        etlapDesing.etelekKiirasa(index+1,etelek[index][0],etelek[index][1])
        if index == 5:
            break
        index+=1

    etlapDesing.szovegKiiras("_" * 6, "Desszertek", "_" * 6)
    print("")
    index = 6
    while index < len(etelek):
        etlapDesing.etelekKiirasa(index+1, etelek[index][0],etelek[index][1])
        index+=1
    etlapDesing.jel("_", 30)
    print("")