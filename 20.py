"""Co otrzymamy po wydrukowaniu poniższych zmiennych?"""
L = [1, 2, 3, 4, 5, 6]
L1 = [x for x in range(5)] # [0, 1, 2, 3, 4]
L2 = [x ** 2 for x in L] # [1, 4, 9, 16, 25, 36]
L3 = [x for x in L if x % 2 == 0] # [2, 4, 6]
L4 = ['Parzysta' if x % 2 == 0 else 'Nieparzysta' for x in range(5)]
    # ['Parzysta', 'Nieparzysta', 'Parzysta', 'Nieparzysta', 'Parzysta']
L5 = [(x, x + 10) for x in L] # [(1, 11), (2, 12), (3, 13), (4, 14), (5, 15), (6, 16)]
D1 = {x: x % 2 == 0 for x in L} # {1: False, 2: True, 3: False, 4: True, 5: False, 6: True}

print(L)
print(L1)
print(L2)
print(L3)
print(L4)
print(L5)
print(D1)