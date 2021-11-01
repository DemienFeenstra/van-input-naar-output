# de speelhal-dag

txt = "Dit geweldige dagje-uit met"
txt2 = "mensen in de Speelhal met"
txt3 = " minuten VR kost je maar"
txt4 = "cent"

Personen = int(input("AantalPersonen"))
Toegangsticket = int(input("Toegangstickets"))
GameSeat = int(input("GameSeats"))
GameSeatTijd = int(input("GameSeatTijd"))

totaal = Personen * Toegangsticket + GameSeatTijd * 9 * 4 * GameSeat

print(txt, Personen, txt2, GameSeatTijd * 9, txt3, totaal, txt4)



# Personen = 4
# Toegangsticket = 7.45
# GameSeat = 0.37
# GameSeatTijd = 5
