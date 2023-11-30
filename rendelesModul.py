

def rendelesModulMain():
    print("Udvozoljuk az etteremben")
    rendelesFelvetel()


def rendelesFelvetel(lista):
    rendeltLista = []
    veglegesFizetesAr: int = 0
    index = 0
    while index < len(lista):
        bekeresKaja = int(input("Kérem a kajának a sorszámát"))
        if bekeresKaja == 1:
            rendeltLista.append(str(lista[index-1]))
            veglegesFizetesAr += 3000
        if bekeresKaja == 2:
            rendeltLista.append(str(lista[index-1]))
            veglegesFizetesAr += 2500
        if bekeresKaja == 3:
            rendeltLista.append(str(lista[index-1]))
            veglegesFizetesAr += 4000
        index+=1
    print(f"Végleges ár {veglegesFizetesAr}")





