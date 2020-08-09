"""Z poniższej listy wypisz stringa ‘schowany’:"""

L = [[34, False], [0], [('abc', 123), {'a': 1, 'x': (True, 'schowany', 5)}]]

print(L[2][1]['x'][1])
