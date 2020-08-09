"""Napisz funkcję, która sprawdzi, czy podany string
zaczyna się słowem "python" i kończy rozszerzeniem
".py".
Przetestuj nią stringi:"""
a = "python_moj_kod.py"
b = "python_notatki.txt"


def check_py(file):
    return file[:6] == "python" and file[-2:] == "py"


print(check_py(a))
print(check_py(b))
