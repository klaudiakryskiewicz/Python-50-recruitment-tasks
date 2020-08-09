"""Stwórz plik o nazwie "moj_plik.txt".
Wpisz do niego liczby od 1 do 100, każdą w nowej linijce.
Otwórz plik i zapisz jego zawartość do listy z_pliku."""

file = open('moj_plik.txt', 'w')

for i in range(1, 101):
    file.write(str(i) + "\n")

file.close()

file = open('moj_plik.txt', 'r')
z_pliku = []
for line in file:
    z_pliku.append(int(line))

print(z_pliku)
