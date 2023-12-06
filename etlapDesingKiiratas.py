import etlapDesing

def kiiras(etelek):


    etlapDesing.jel("*", 30)
    etlapDesing.etteremMegnevezes("Borsodi etterem")
    etlapDesing.jel("*", 30)

    # etlapDesing.szovegKiiras("_" * 6, "Levesek", "_" * 6)
    # print("")
    # index = 0
    # while index < len(etelek):
    #     etlapDesing.etelekKiirasa(index+1,etelek[index][0],etelek[index][1])
    #     if index == 2:
    #         break
    #     index+=1
    # etlapDesing.szovegKiiras("_" * 6, "Foetel", "_" * 6)
    # print("")
    # index = 3
    # while index < len(etelek):
    #     etlapDesing.etelekKiirasa(index+1,etelek[index][0],etelek[index][1])
    #     if index == 5:
    #         break
    #     index+=1
    #
    # etlapDesing.szovegKiiras("_" * 6, "Desszertek", "_" * 6)
    # print("")
    # index = 6
    # while index < len(etelek):
    #     etlapDesing.etelekKiirasa(index+1, etelek[index][0],etelek[index][1])
    #     index+=1
    # print("")
    # etlapDesing.jel("_", 30)
    index = 0
    while index < len(etelek):
        etlapDesing.etelekKiirasa(index+1, etelek[index][0],etelek[index][1])
        index+=1
    etlapDesing.jel("_", 30)
