"""Korzystając z podanej listy A, stwórz listę B, która będzie
zawierać tylko unikalne elementy z listy A."""

#1st way
A = [1,2,3,3,2,1,2,3]
B = []
for i in A:
    if i not in B:
        B.append(i)

print(B)

#2nd way
C = list(set(A))
print(C)
