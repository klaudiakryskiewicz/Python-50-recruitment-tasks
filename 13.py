"""Stwórz dwie listy:
A – zawierającą liczby od 1 do 10.
B – zawierającą co trzecią liczbę z zakresu od 100 do 1.
W obu przypadkach możesz napisać tylko jedną linijkę kodu."""

A = [i for i in range(1, 11)]
print(A)

B = [i for i in range(100, 0, -3)]
print(B)
