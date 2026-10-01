
invoer = float(input("Geef prijs boek: "))
basis = invoer
invoer = int(input("Geef het aantal boeken: "))
aantal = invoer
inkoop = 0.60* basis
eerst = 3.00
volgend = 0.75
som = aantal * inkoop + eerst + (aantal - 1) * volgend
print('de totale kost is: ', som)

