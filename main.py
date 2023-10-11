import etlapDesing
import rendelesModul

etlapDesing.jel("*", 30)
etlapDesing.etteremMegnevezes("Borsodi etterem")
etlapDesing.jel("*", 30)

etlapDesing.szovegKiiras("_" * 6, "Levesek", "_" * 6)
print("")
etlapDesing.etelekKiirasa("gazpacho", 3000, "ft")
etlapDesing.etelekKiirasa("husleves", 2500, "ft")
etlapDesing.etelekKiirasa("kremleves", 2250, "ft")

etlapDesing.szovegKiiras("_" * 6, "Foetel", "_" * 6)
print("")
etlapDesing.etelekKiirasa("sertesbelszin", 3500, "ft")
etlapDesing.etelekKiirasa("lazacfile", 6000, "ft")
etlapDesing.etelekKiirasa("gombas rizotto", 4800, "ft")

etlapDesing.szovegKiiras("_" * 6, "Desszertek", "_" * 6)
print("")
etlapDesing.etelekKiirasa("csokoladetorta", 3000, "ft")
etlapDesing.etelekKiirasa("citrusos panna", 4700, "ft")
etlapDesing.etelekKiirasa("sozott csokigolyo", 7500, "ft")
etlapDesing.jel("_", 30)
print("")
rendelesModul.rendelesModulMain()
