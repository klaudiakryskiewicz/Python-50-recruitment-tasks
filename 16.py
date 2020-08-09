"""Wypisz podaną listę imion, przed każdym dodając
kolejny numer. Zacznij numerowanie od 1."""

imiona = ["Adam", 'Stanisław', 'Maria', 'Zofia', "Mikołaj"]

i = 1
for imie in imiona:
    print(i, imie)
    i += 1

for counter, value in enumerate(imiona, 1):
    print(counter, value)
