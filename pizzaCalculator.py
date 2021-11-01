# Demiën Feenstra Opdracht: Pizza Calculator

SmallPizza = input("Hoeveel small pizza's wilt u bestellen? (kosten: 3 euro p/s)")
MediumPizza = input("Hoeveel medium pizza's wilt u bestellen? (kosten: 5 euro p/s)")
LargePizza = input("Hoeveel large pizza's wilt u bestellen? (kosten: 7 euro p/s)")

SmallPrijs = (SmallPizza * 3)
MediumPrijs = (MediumPizza * 5)
LargePrijs = (LargePizza * 7)

print("u heeft" + " " + SmallPizza + " " + "small pizza('s) besteld")
print("u heeft" + " " + MediumPizza + " " + "medium pizza('s) besteld")
print("u heeft" + " " + LargePizza + " " + "large pizza('s) besteld")

print(SmallPrijs + " " + "euro voor de small pizza('s)")
print(MediumPrijs + " " + "euro voor de medium pizza('s)")
print(LargePrijs + " " + "euro voor de large pizza('s)")

totaal = (SmallPrijs + MediumPrijs + LargePrijs)
print("te betalen:" + " " + totaal + " " + "euro")
