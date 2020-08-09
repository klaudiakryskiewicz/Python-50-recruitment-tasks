"""Jakiej struktury danych użyłbyś do zamodelowania
szafki, która ma 3 szuflady, a w każdej z nich znajdują się
3 przegródki?
Stwórz taki model i umieść stringa "długopis" w
środkowej przegródce środkowej szuflady"""

szafka = [[[], [], []], [[], [], []], [[], [], []]]

szafka[1][1].append("długopis")
print(szafka)

for szuflada in szafka:
    print(f"Szuflada {szafka.index(szuflada) + 1}: {szuflada}")