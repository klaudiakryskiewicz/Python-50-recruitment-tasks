"""Napisz funkcję, która będzie pobierać dwie liczby
i sprawdzać, czy pierwsza z nich jest podzielna przez
drugą."""


def check_divisibility(a, b):
    return a % b == 0


print(check_divisibility(5, 3))
print(check_divisibility(25, 5))
