# feestlunch

txt = "De feestlunch kost je bij de bakker"
txt2 = "cent voor de" 
txt3 = "croissantjes en de"
txt4 = "stokbroden als de"
txt5 = "kortingsbonnen nog geldig zijn!"

AantalCroissantjes = int(input("AantalCroissantjes"))
CroissantPrijs = int(input("CroissantPrijs"))

AantalStokbroden = int(input("AantalStokbroden"))
StokbroodPrijs = int(input("StokbroodPrijs"))

AantalKortingsbonnen = int(input("AantalKortingsbonnen"))
KortingsbonWaarde = int(input("KortingsbonWaarde"))

totaal = AantalCroissantjes * CroissantPrijs + AantalStokbroden * StokbroodPrijs - AantalKortingsbonnen * KortingsbonWaarde
print(txt, totaal, txt2, AantalCroissantjes, txt3, AantalStokbroden, txt4, AantalKortingsbonnen, txt5)

# 17 
# 0.39
# 2
# 2.78
# 3
# 0.50
