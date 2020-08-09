"""Objętość graniastosłupa oblicza się na podstawie wzoru:
V = a * b * h. Długości boków podstawy to a i b, zaś h to
wysokość.
Poniższy kod znajduj największy
graniastosłup jaki możemy utworzyć z elementów list A,
B i H. Ile operacji zostanie wykonane w wyniku
uruchomienia tego kodu? W jaki sposób można by to
zadanie rozwiązać bardziej efektywnie?"""
import random

A = [random.randint(0, 100) for i in range(5)]
B = [random.randint(0, 100) for i in range(5)]
H = [random.randint(0, 100) for i in range(5)]
max_v = 0
for a in A:
    for b in B:
        for h in H:
            if a * b * h > max_v:
                max_v = a * b * h

print(max_v)

max_v = max(A)*max(B)*max(H)
print(max_v)