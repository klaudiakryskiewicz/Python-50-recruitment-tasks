"""Co zostanie wypisane w wyniku wykonania poniższego
kodu?"""
A = [1, 2, 3, 4, 5]
B = A  # referencja do A
C = A[:]  # C = list(A) - stworzenie kopii danych z A
B[0] = 111
print(A, B, C)
