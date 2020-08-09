"""Na podstawie listy jezyki stwórz listę jezyki_odwrocone
zawierającą elementy listy jezyki w odwróconej
kolejności."""

jezyki = ['Python', 'Java', 'C#', 'Ruby']

#1st way
jezyki_odwrocone = list(reversed(jezyki))
print(jezyki_odwrocone)

#2nd way
jezyki_odwrocone2 = jezyki[::-1]
print(jezyki_odwrocone2)

#3rd way
jezyki_odwrocone3 = jezyki
jezyki_odwrocone3.reverse()
print(jezyki_odwrocone3)