"""Otrzymujesz listę nazwisk, jakie klienci wprowadzili
w formularz na stronie internetowej.
Użyj funkcji filter(), aby usunąć z niego wszystkie wpisy,
które nie są stringami.
Użyj funkcji map(), aby przerobić nazwiska tak, żeby
wszystkie były zapisane poprawnie z wielkimi literami
tylko na początku imienia i nazwiska.
"""
from string import capwords

nazwiska = ['jan kot', 18, 'ANNA KRÓL', 'jÓzef BYK',
['nie', 'wasza','sprawa'], 'ROBERT wąŻ']

nazwiska_ = list(filter(lambda x: type(x) is str, nazwiska))

nazwiska_final = list(map(lambda x: capwords(x), nazwiska_))

print(nazwiska_final)